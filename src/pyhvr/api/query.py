"""Query interface."""

from __future__ import annotations

from typing import Any


class QueryMixin:
    def query_channels(self, hub: str) -> dict[str, Any]:
        return self._request("GET", f"/hubs/{hub}/query/channels")

    def query_channel_locs(self, hub: str, channel: str) -> dict[str, Any]:
        return self._request("GET", f"/hubs/{hub}/query/channels/{channel}/locs")

    def query_channel_loc_table(self, hub: str, channel: str, loc: str, table: str) -> dict[str, Any]:
        return self._request("GET", f"/hubs/{hub}/query/channels/{channel}/locs/{loc}/tables/{table}")

    def query_channel_tables(self, hub: str, channel: str) -> dict[str, Any]:
        return self._request("GET", f"/hubs/{hub}/query/channels/{channel}/tables")

    def query_hub_status(self, hub: str) -> dict[str, Any]:
        return self._request("GET", f"/hubs/{hub}/query/status")


class AsyncQueryMixin:
    async def query_channels(self, hub: str) -> dict[str, Any]:
        return await self._request("GET", f"/hubs/{hub}/query/channels")

    async def query_channel_locs(self, hub: str, channel: str) -> dict[str, Any]:
        return await self._request("GET", f"/hubs/{hub}/query/channels/{channel}/locs")

    async def query_channel_loc_table(self, hub: str, channel: str, loc: str, table: str) -> dict[str, Any]:
        return await self._request("GET", f"/hubs/{hub}/query/channels/{channel}/locs/{loc}/tables/{table}")

    async def query_channel_tables(self, hub: str, channel: str) -> dict[str, Any]:
        return await self._request("GET", f"/hubs/{hub}/query/channels/{channel}/tables")

    async def query_hub_status(self, hub: str) -> dict[str, Any]:
        return await self._request("GET", f"/hubs/{hub}/query/status")
