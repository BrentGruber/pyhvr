"""Tests for auth, transport, context manager, and exception handling."""

import time

import httpx
import pytest
import respx

from pyhvr import AsyncHvrClient, HvrClient
from pyhvr.exceptions import ConnectionError, LoginError, RestError

BASE = "http://hvr.test:4340"
LOGIN_RESPONSE = {
    "token_type": "bearer",
    "access_token": "tok123",
    "expires_in": 900,
    "refresh_token": "ref456",
}


@respx.mock
def test_sync_context_manager_login():
    respx.post(f"{BASE}/auth/v1/password").mock(return_value=httpx.Response(200, json=LOGIN_RESPONSE))
    respx.get(f"{BASE}/api/latest/hubs").mock(return_value=httpx.Response(200, json={"result": []}))

    with HvrClient(base_url=BASE, username="admin", password="secret") as client:
        result = client.list_hubs()

    assert result == {"result": []}


@pytest.mark.asyncio
@respx.mock
async def test_async_context_manager_login():
    respx.post(f"{BASE}/auth/v1/password").mock(return_value=httpx.Response(200, json=LOGIN_RESPONSE))
    respx.get(f"{BASE}/api/latest/hubs").mock(return_value=httpx.Response(200, json={"result": []}))

    async with AsyncHvrClient(base_url=BASE, username="admin", password="secret") as client:
        result = await client.list_hubs()

    assert result == {"result": []}


@respx.mock
def test_login_failure_raises_login_error():
    respx.post(f"{BASE}/auth/v1/password").mock(return_value=httpx.Response(403, text="Forbidden"))

    client = HvrClient(base_url=BASE, username="admin", password="wrong")
    with pytest.raises(LoginError, match="Login failed"):
        client.__enter__()


@respx.mock
def test_rest_error_on_4xx():
    respx.post(f"{BASE}/auth/v1/password").mock(return_value=httpx.Response(200, json=LOGIN_RESPONSE))
    respx.get(f"{BASE}/api/latest/hubs").mock(
        return_value=httpx.Response(400, json={"message": "F_JR0001Y bad request detail"})
    )

    with HvrClient(base_url=BASE, username="admin", password="secret") as client:
        with pytest.raises(RestError) as exc_info:
            client.list_hubs()

    err = exc_info.value
    assert err.status_code == 400
    assert err.error_code == "F_JR0001"
    assert "bad request detail" in err.detail


@respx.mock
def test_connection_error_on_connect_failure():
    respx.post(f"{BASE}/auth/v1/password").mock(side_effect=httpx.ConnectError("refused"))

    client = HvrClient(base_url=BASE, username="admin", password="secret")
    with pytest.raises(ConnectionError, match="Cannot connect"):
        client.__enter__()


@respx.mock
def test_token_refresh_when_expired():
    respx.post(f"{BASE}/auth/v1/password").mock(return_value=httpx.Response(200, json=LOGIN_RESPONSE))
    refresh_response = {**LOGIN_RESPONSE, "access_token": "new_tok", "refresh_token": "new_ref"}
    respx.post(f"{BASE}/auth/v1/refresh").mock(return_value=httpx.Response(200, json=refresh_response))
    respx.get(f"{BASE}/api/latest/hubs").mock(return_value=httpx.Response(200, json={}))

    with HvrClient(base_url=BASE, username="admin", password="secret") as client:
        # Force token to be expired
        client._token_expires_at = time.monotonic() - 1
        client.list_hubs()

    assert client._access_token == "new_tok"


@respx.mock
def test_token_refresh_falls_back_to_login_on_error():
    login_count = {"n": 0}
    original_response = {**LOGIN_RESPONSE}
    second_login_response = {**LOGIN_RESPONSE, "access_token": "tok_after_relogin"}

    def login_side_effect(request):
        login_count["n"] += 1
        if login_count["n"] == 1:
            return httpx.Response(200, json=original_response)
        return httpx.Response(200, json=second_login_response)

    respx.post(f"{BASE}/auth/v1/password").mock(side_effect=login_side_effect)
    respx.post(f"{BASE}/auth/v1/refresh").mock(return_value=httpx.Response(401, text="expired"))
    respx.get(f"{BASE}/api/latest/hubs").mock(return_value=httpx.Response(200, json={}))

    with HvrClient(base_url=BASE, username="admin", password="secret") as client:
        client._token_expires_at = time.monotonic() - 1
        client.list_hubs()

    assert client._access_token == "tok_after_relogin"


@respx.mock
def test_none_returned_for_empty_response():
    respx.post(f"{BASE}/auth/v1/password").mock(return_value=httpx.Response(200, json=LOGIN_RESPONSE))
    respx.delete(f"{BASE}/api/latest/hubs/myhub").mock(return_value=httpx.Response(200, content=b""))

    with HvrClient(base_url=BASE, username="admin", password="secret") as client:
        result = client.delete_hub("myhub")

    assert result is None


@pytest.mark.asyncio
@respx.mock
async def test_async_rest_error():
    respx.post(f"{BASE}/auth/v1/password").mock(return_value=httpx.Response(200, json=LOGIN_RESPONSE))
    respx.get(f"{BASE}/api/latest/hubs").mock(
        return_value=httpx.Response(403, json={"message": "F_JR0002Y forbidden"})
    )

    async with AsyncHvrClient(base_url=BASE, username="admin", password="secret") as client:
        with pytest.raises(RestError) as exc_info:
            await client.list_hubs()

    assert exc_info.value.status_code == 403


@respx.mock
def test_custom_api_version():
    respx.post(f"{BASE}/auth/v1/password").mock(return_value=httpx.Response(200, json=LOGIN_RESPONSE))
    respx.get(f"{BASE}/api/v6.1.0.3/hubs").mock(return_value=httpx.Response(200, json={}))

    with HvrClient(base_url=BASE, username="admin", password="secret", api_version="v6.1.0.3") as client:
        client.list_hubs()

    assert respx.calls.last.request.url.path == "/api/v6.1.0.3/hubs"


@respx.mock
def test_text_response_returned_for_non_json():
    respx.post(f"{BASE}/auth/v1/password").mock(return_value=httpx.Response(200, json=LOGIN_RESPONSE))
    respx.get(f"{BASE}/api/latest/logs/hvr.log").mock(
        return_value=httpx.Response(200, text="some log text", headers={"content-type": "text/plain"})
    )

    with HvrClient(base_url=BASE, username="admin", password="secret") as client:
        result = client.get_log("hvr.log")

    assert result == "some log text"
