"""Event interface."""

from __future__ import annotations

from typing import Any


class EventMixin:
    def get_event_channels(self, hub: str) -> dict[str, Any]:
        return self._request("GET", f"/hubs/{hub}/event_channels")

    def get_event_locs(self, hub: str) -> dict[str, Any]:
        return self._request("GET", f"/hubs/{hub}/event_locs")

    def get_event_types(self, hub: str) -> dict[str, Any]:
        return self._request("GET", f"/hubs/{hub}/event_types")

    def list_events(self, hub: str) -> dict[str, Any]:
        return self._request("GET", f"/hubs/{hub}/events")

    def get_event_log(self, hub: str, ev_id: str) -> dict[str, Any]:
        return self._request("GET", f"/hubs/{hub}/events/{ev_id}/log")

    def get_repo_event_types(self) -> dict[str, Any]:
        return self._request("GET", "/repos/event_types")

    def get_repo_events(self) -> dict[str, Any]:
        return self._request("GET", "/repos/events")

    def cancel_events(self, hub: str, body: dict | None = None) -> dict[str, Any]:
        return self._request("POST", f"/hubs/{hub}/events_cancel", json=body)


class AsyncEventMixin:
    async def get_event_channels(self, hub: str) -> dict[str, Any]:
        return await self._request("GET", f"/hubs/{hub}/event_channels")

    async def get_event_locs(self, hub: str) -> dict[str, Any]:
        return await self._request("GET", f"/hubs/{hub}/event_locs")

    async def get_event_types(self, hub: str) -> dict[str, Any]:
        return await self._request("GET", f"/hubs/{hub}/event_types")

    async def list_events(self, hub: str) -> dict[str, Any]:
        return await self._request("GET", f"/hubs/{hub}/events")

    async def get_event_log(self, hub: str, ev_id: str) -> dict[str, Any]:
        return await self._request("GET", f"/hubs/{hub}/events/{ev_id}/log")

    async def get_repo_event_types(self) -> dict[str, Any]:
        return await self._request("GET", "/repos/event_types")

    async def get_repo_events(self) -> dict[str, Any]:
        return await self._request("GET", "/repos/events")

    async def cancel_events(self, hub: str, body: dict | None = None) -> dict[str, Any]:
        return await self._request("POST", f"/hubs/{hub}/events_cancel", json=body)
