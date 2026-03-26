"""Tests for Jobs, Alerts, Hubs, and other interface groups."""

import httpx
import pytest
import respx

from pyhvr import AsyncHvrClient, HvrClient

BASE = "http://hvr.test:4340"
LOGIN = {
    "token_type": "bearer",
    "access_token": "tok",
    "expires_in": 900,
    "refresh_token": "ref",
}


# --- Jobs ---


@respx.mock
def test_list_jobs():
    respx.post(f"{BASE}/auth/v1/password").mock(return_value=httpx.Response(200, json=LOGIN))
    respx.get(f"{BASE}/api/latest/hubs/h1/jobs").mock(
        return_value=httpx.Response(200, json={"jobs": []})
    )
    with HvrClient(BASE, "u", "p") as c:
        result = c.list_jobs("h1")
    assert "jobs" in result


@respx.mock
def test_start_jobs():
    respx.post(f"{BASE}/auth/v1/password").mock(return_value=httpx.Response(200, json=LOGIN))
    respx.post(f"{BASE}/api/latest/hubs/h1/jobs_start").mock(
        return_value=httpx.Response(200, json={"started": True})
    )
    with HvrClient(BASE, "u", "p") as c:
        result = c.start_jobs("h1", body={"jobs": ["j1"]})
    assert result["started"] is True


@respx.mock
def test_delete_job_env_var():
    respx.post(f"{BASE}/auth/v1/password").mock(return_value=httpx.Response(200, json=LOGIN))
    respx.delete(f"{BASE}/api/latest/hubs/h1/jobs/j1/env_vars/MY_VAR").mock(
        return_value=httpx.Response(200, content=b"")
    )
    with HvrClient(BASE, "u", "p") as c:
        result = c.delete_job_env_var("h1", "j1", "MY_VAR")
    assert result is None


# --- Alerts ---


@respx.mock
def test_list_alerts():
    respx.post(f"{BASE}/auth/v1/password").mock(return_value=httpx.Response(200, json=LOGIN))
    respx.get(f"{BASE}/api/latest/hubs/h1/alerts").mock(
        return_value=httpx.Response(200, json={"alerts": []})
    )
    with HvrClient(BASE, "u", "p") as c:
        result = c.list_alerts("h1")
    assert "alerts" in result


@respx.mock
def test_delete_alert():
    respx.post(f"{BASE}/auth/v1/password").mock(return_value=httpx.Response(200, json=LOGIN))
    respx.delete(f"{BASE}/api/latest/hubs/h1/alerts/a1").mock(
        return_value=httpx.Response(200, content=b"")
    )
    with HvrClient(BASE, "u", "p") as c:
        result = c.delete_alert("h1", "a1")
    assert result is None


# --- Hubs ---


@respx.mock
def test_create_hub():
    respx.post(f"{BASE}/auth/v1/password").mock(return_value=httpx.Response(200, json=LOGIN))
    respx.post(f"{BASE}/api/latest/hubs").mock(
        return_value=httpx.Response(201, json={"hub": "newhub"})
    )
    with HvrClient(BASE, "u", "p") as c:
        result = c.create_hub(body={"name": "newhub"})
    assert result["hub"] == "newhub"


@respx.mock
def test_delete_hub():
    respx.post(f"{BASE}/auth/v1/password").mock(return_value=httpx.Response(200, json=LOGIN))
    respx.delete(f"{BASE}/api/latest/hubs/h1").mock(
        return_value=httpx.Response(200, content=b"")
    )
    with HvrClient(BASE, "u", "p") as c:
        result = c.delete_hub("h1")
    assert result is None


# --- Events ---


@respx.mock
def test_list_events():
    respx.post(f"{BASE}/auth/v1/password").mock(return_value=httpx.Response(200, json=LOGIN))
    respx.get(f"{BASE}/api/latest/hubs/h1/events").mock(
        return_value=httpx.Response(200, json={"events": []})
    )
    with HvrClient(BASE, "u", "p") as c:
        result = c.list_events("h1")
    assert "events" in result


# --- Misc ---


@respx.mock
def test_list_api_versions():
    respx.post(f"{BASE}/auth/v1/password").mock(return_value=httpx.Response(200, json=LOGIN))
    respx.get(f"{BASE}/api/latest/api").mock(
        return_value=httpx.Response(200, json=["v0", "v6.1.0.3", "latest"])
    )
    with HvrClient(BASE, "u", "p") as c:
        result = c.list_api_versions()
    assert "latest" in result


# --- Users ---


@respx.mock
def test_list_users():
    respx.post(f"{BASE}/auth/v1/password").mock(return_value=httpx.Response(200, json=LOGIN))
    respx.get(f"{BASE}/api/latest/users").mock(
        return_value=httpx.Response(200, json={"users": []})
    )
    with HvrClient(BASE, "u", "p") as c:
        result = c.list_users()
    assert "users" in result


# --- Async ---


@pytest.mark.asyncio
@respx.mock
async def test_async_list_channels():
    respx.post(f"{BASE}/auth/v1/password").mock(return_value=httpx.Response(200, json=LOGIN))
    respx.get(f"{BASE}/api/latest/hubs/h1/definition/channels").mock(
        return_value=httpx.Response(200, json={"channels": []})
    )
    async with AsyncHvrClient(BASE, "u", "p") as c:
        result = await c.list_channels("h1")
    assert "channels" in result


@pytest.mark.asyncio
@respx.mock
async def test_async_start_jobs():
    respx.post(f"{BASE}/auth/v1/password").mock(return_value=httpx.Response(200, json=LOGIN))
    respx.post(f"{BASE}/api/latest/hubs/h1/jobs_start").mock(
        return_value=httpx.Response(200, json={"ok": True})
    )
    async with AsyncHvrClient(BASE, "u", "p") as c:
        result = await c.start_jobs("h1")
    assert result["ok"] is True
