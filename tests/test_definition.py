"""Tests for the Definition interface."""

import httpx
import respx

from pyhvr import HvrClient

BASE = "http://hvr.test:4340"
LOGIN = {
    "token_type": "bearer",
    "access_token": "tok",
    "expires_in": 900,
    "refresh_token": "ref",
}


@respx.mock
def test_list_channels():
    respx.post(f"{BASE}/auth/v1/password").mock(return_value=httpx.Response(200, json=LOGIN))
    respx.get(f"{BASE}/api/latest/hubs/h1/definition/channels").mock(
        return_value=httpx.Response(200, json={"channels": ["ch1"]})
    )
    with HvrClient(BASE, "u", "p") as c:
        result = c.list_channels("h1")
    assert result == {"channels": ["ch1"]}


@respx.mock
def test_create_channel():
    respx.post(f"{BASE}/auth/v1/password").mock(return_value=httpx.Response(200, json=LOGIN))
    respx.post(f"{BASE}/api/latest/hubs/h1/definition/channels").mock(
        return_value=httpx.Response(201, json={"name": "ch_new"})
    )
    with HvrClient(BASE, "u", "p") as c:
        result = c.create_channel("h1", body={"name": "ch_new"})
    assert result["name"] == "ch_new"


@respx.mock
def test_delete_channel():
    respx.post(f"{BASE}/auth/v1/password").mock(return_value=httpx.Response(200, json=LOGIN))
    respx.delete(f"{BASE}/api/latest/hubs/h1/definition/channels/ch1").mock(
        return_value=httpx.Response(200, content=b"")
    )
    with HvrClient(BASE, "u", "p") as c:
        result = c.delete_channel("h1", "ch1")
    assert result is None


@respx.mock
def test_patch_channel():
    respx.post(f"{BASE}/auth/v1/password").mock(return_value=httpx.Response(200, json=LOGIN))
    respx.patch(f"{BASE}/api/latest/hubs/h1/definition/channels/ch1").mock(
        return_value=httpx.Response(200, json={"updated": True})
    )
    with HvrClient(BASE, "u", "p") as c:
        result = c.patch_channel("h1", "ch1", body={"prop": "val"})
    assert result == {"updated": True}


@respx.mock
def test_list_locs():
    respx.post(f"{BASE}/auth/v1/password").mock(return_value=httpx.Response(200, json=LOGIN))
    respx.get(f"{BASE}/api/latest/hubs/h1/definition/locs").mock(
        return_value=httpx.Response(200, json={"locs": ["src", "tgt"]})
    )
    with HvrClient(BASE, "u", "p") as c:
        result = c.list_locs("h1")
    assert "locs" in result
