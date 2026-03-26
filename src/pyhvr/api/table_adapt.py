"""Table Adapt interface."""

from __future__ import annotations

from typing import Any


class TableAdaptMixin:
    def apply_table_adapt(self, hub: str, channel: str, loc: str, body: dict | None = None) -> dict[str, Any]:
        return self._request("POST", f"/hubs/{hub}/channels/{channel}/locs/{loc}/adapt/apply", json=body)

    def adapt_other_channels(self, hub: str, channel: str, loc: str, body: dict | None = None) -> dict[str, Any]:
        return self._request("POST", f"/hubs/{hub}/channels/{channel}/locs/{loc}/adapt/other_channels", json=body)

    def adapt_slicing(self, hub: str, channel: str, loc: str, body: dict | None = None) -> dict[str, Any]:
        return self._request("POST", f"/hubs/{hub}/channels/{channel}/locs/{loc}/adapt/slicing", json=body)

    def get_slicing_boundaries(self, hub: str, channel: str, loc: str, table: str, body: dict | None = None) -> dict[str, Any]:
        return self._request("POST", f"/hubs/{hub}/channels/{channel}/locs/{loc}/tables/{table}/slicing_boundaries", json=body)


class AsyncTableAdaptMixin:
    async def apply_table_adapt(self, hub: str, channel: str, loc: str, body: dict | None = None) -> dict[str, Any]:
        return await self._request("POST", f"/hubs/{hub}/channels/{channel}/locs/{loc}/adapt/apply", json=body)

    async def adapt_other_channels(self, hub: str, channel: str, loc: str, body: dict | None = None) -> dict[str, Any]:
        return await self._request("POST", f"/hubs/{hub}/channels/{channel}/locs/{loc}/adapt/other_channels", json=body)

    async def adapt_slicing(self, hub: str, channel: str, loc: str, body: dict | None = None) -> dict[str, Any]:
        return await self._request("POST", f"/hubs/{hub}/channels/{channel}/locs/{loc}/adapt/slicing", json=body)

    async def get_slicing_boundaries(self, hub: str, channel: str, loc: str, table: str, body: dict | None = None) -> dict[str, Any]:
        return await self._request("POST", f"/hubs/{hub}/channels/{channel}/locs/{loc}/tables/{table}/slicing_boundaries", json=body)
