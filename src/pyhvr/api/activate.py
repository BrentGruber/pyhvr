"""Activate, Refresh, and Compare interface."""

from __future__ import annotations

from typing import Any


class ActivateMixin:
    def get_hub_activate(self, hub: str) -> dict[str, Any]:
        return self._request("GET", f"/hubs/{hub}/activate")

    def get_channel_activate(self, hub: str, channel: str) -> dict[str, Any]:
        return self._request("GET", f"/hubs/{hub}/channels/{channel}/activate")

    def get_loc_activate(self, hub: str, loc: str) -> dict[str, Any]:
        return self._request("GET", f"/hubs/{hub}/locs/{loc}/activate")

    def get_channel_refresh_table_result_ids(self, hub: str, channel: str) -> dict[str, Any]:
        return self._request("GET", f"/hubs/{hub}/channels/{channel}/refresh/tables_results_ids")

    def get_hub_refresh_table_result_ids(self, hub: str) -> dict[str, Any]:
        return self._request("GET", f"/hubs/{hub}/refresh/tables_results_ids")

    def get_channel_compare_table_result_ids(self, hub: str, channel: str) -> dict[str, Any]:
        return self._request("GET", f"/hubs/{hub}/channels/{channel}/compare/tables_results_ids")

    def get_channel_contexts(self, hub: str, channel: str) -> dict[str, Any]:
        return self._request("GET", f"/hubs/{hub}/channels/{channel}/contexts")

    def activate_channel(self, hub: str, channel: str, body: dict | None = None) -> dict[str, Any]:
        return self._request("POST", f"/hubs/{hub}/channels/{channel}/activate", json=body)

    def deactivate_channel(self, hub: str, channel: str, body: dict | None = None) -> dict[str, Any]:
        return self._request("POST", f"/hubs/{hub}/channels/{channel}/deactivate", json=body)

    def compare_channel(self, hub: str, channel: str, body: dict | None = None) -> dict[str, Any]:
        return self._request("POST", f"/hubs/{hub}/channels/{channel}/compare", json=body)

    def refresh_channel(self, hub: str, channel: str, body: dict | None = None) -> dict[str, Any]:
        return self._request("POST", f"/hubs/{hub}/channels/{channel}/refresh", json=body)


class AsyncActivateMixin:
    async def get_hub_activate(self, hub: str) -> dict[str, Any]:
        return await self._request("GET", f"/hubs/{hub}/activate")

    async def get_channel_activate(self, hub: str, channel: str) -> dict[str, Any]:
        return await self._request("GET", f"/hubs/{hub}/channels/{channel}/activate")

    async def get_loc_activate(self, hub: str, loc: str) -> dict[str, Any]:
        return await self._request("GET", f"/hubs/{hub}/locs/{loc}/activate")

    async def get_channel_refresh_table_result_ids(self, hub: str, channel: str) -> dict[str, Any]:
        return await self._request("GET", f"/hubs/{hub}/channels/{channel}/refresh/tables_results_ids")

    async def get_hub_refresh_table_result_ids(self, hub: str) -> dict[str, Any]:
        return await self._request("GET", f"/hubs/{hub}/refresh/tables_results_ids")

    async def get_channel_compare_table_result_ids(self, hub: str, channel: str) -> dict[str, Any]:
        return await self._request("GET", f"/hubs/{hub}/channels/{channel}/compare/tables_results_ids")

    async def get_channel_contexts(self, hub: str, channel: str) -> dict[str, Any]:
        return await self._request("GET", f"/hubs/{hub}/channels/{channel}/contexts")

    async def activate_channel(self, hub: str, channel: str, body: dict | None = None) -> dict[str, Any]:
        return await self._request("POST", f"/hubs/{hub}/channels/{channel}/activate", json=body)

    async def deactivate_channel(self, hub: str, channel: str, body: dict | None = None) -> dict[str, Any]:
        return await self._request("POST", f"/hubs/{hub}/channels/{channel}/deactivate", json=body)

    async def compare_channel(self, hub: str, channel: str, body: dict | None = None) -> dict[str, Any]:
        return await self._request("POST", f"/hubs/{hub}/channels/{channel}/compare", json=body)

    async def refresh_channel(self, hub: str, channel: str, body: dict | None = None) -> dict[str, Any]:
        return await self._request("POST", f"/hubs/{hub}/channels/{channel}/refresh", json=body)
