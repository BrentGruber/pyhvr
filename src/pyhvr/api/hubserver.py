"""HubServer interface."""

from __future__ import annotations

from typing import Any


class HubServerMixin:
    def get_hubserver_clock(self) -> dict[str, Any]:
        return self._request("GET", "/hubserver/clock")

    def get_hubserver_env_vars(self) -> dict[str, Any]:
        return self._request("GET", "/hubserver/env/vars")

    def get_hubserver_props(self) -> dict[str, Any]:
        return self._request("GET", "/hubserver/props")

    def delete_hubserver_props(self, body: dict | None = None) -> dict[str, Any]:
        return self._request("POST", "/hubserver/props_delete", json=body)

    def test_hubserver_props(self, body: dict | None = None) -> dict[str, Any]:
        return self._request("POST", "/hubserver/props_test", json=body)

    def restart_hubserver(self, body: dict | None = None) -> dict[str, Any]:
        return self._request("POST", "/hubserver/restart", json=body)

    def stop_hubserver(self, body: dict | None = None) -> dict[str, Any]:
        return self._request("POST", "/hubserver/stop", json=body)

    def test_hubserver(self, body: dict | None = None) -> dict[str, Any]:
        return self._request("POST", "/hubserver/test", json=body)

    def upload_to_hubserver(self, body: dict | None = None) -> dict[str, Any]:
        return self._request("POST", "/hubserver/upload", json=body)

    def patch_hubserver_props(self, body: dict | None = None) -> dict[str, Any]:
        return self._request("PATCH", "/hubserver/props", json=body)


class AsyncHubServerMixin:
    async def get_hubserver_clock(self) -> dict[str, Any]:
        return await self._request("GET", "/hubserver/clock")

    async def get_hubserver_env_vars(self) -> dict[str, Any]:
        return await self._request("GET", "/hubserver/env/vars")

    async def get_hubserver_props(self) -> dict[str, Any]:
        return await self._request("GET", "/hubserver/props")

    async def delete_hubserver_props(self, body: dict | None = None) -> dict[str, Any]:
        return await self._request("POST", "/hubserver/props_delete", json=body)

    async def test_hubserver_props(self, body: dict | None = None) -> dict[str, Any]:
        return await self._request("POST", "/hubserver/props_test", json=body)

    async def restart_hubserver(self, body: dict | None = None) -> dict[str, Any]:
        return await self._request("POST", "/hubserver/restart", json=body)

    async def stop_hubserver(self, body: dict | None = None) -> dict[str, Any]:
        return await self._request("POST", "/hubserver/stop", json=body)

    async def test_hubserver(self, body: dict | None = None) -> dict[str, Any]:
        return await self._request("POST", "/hubserver/test", json=body)

    async def upload_to_hubserver(self, body: dict | None = None) -> dict[str, Any]:
        return await self._request("POST", "/hubserver/upload", json=body)

    async def patch_hubserver_props(self, body: dict | None = None) -> dict[str, Any]:
        return await self._request("PATCH", "/hubserver/props", json=body)
