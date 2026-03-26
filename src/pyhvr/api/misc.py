"""Miscellaneous interface."""

from __future__ import annotations

from typing import Any


class MiscMixin:
    def list_api_versions(self) -> list[str]:
        return self._request("GET", "/api")

    def parse_mapdoc(self, hub: str, body: dict | None = None) -> dict[str, Any]:
        return self._request("POST", f"/hubs/{hub}/mapdoc/parse", json=body)

    def create_snapshot(self, body: dict | None = None) -> dict[str, Any]:
        return self._request("POST", "/snapshot", json=body)

    def inspect_snapshot(self, body: dict | None = None) -> dict[str, Any]:
        return self._request("POST", "/snapshot_inspect", json=body)


class AsyncMiscMixin:
    async def list_api_versions(self) -> list[str]:
        return await self._request("GET", "/api")

    async def parse_mapdoc(self, hub: str, body: dict | None = None) -> dict[str, Any]:
        return await self._request("POST", f"/hubs/{hub}/mapdoc/parse", json=body)

    async def create_snapshot(self, body: dict | None = None) -> dict[str, Any]:
        return await self._request("POST", "/snapshot", json=body)

    async def inspect_snapshot(self, body: dict | None = None) -> dict[str, Any]:
        return await self._request("POST", "/snapshot_inspect", json=body)
