"""Control Message interface."""

from __future__ import annotations

from typing import Any


class ControlMixin:
    def get_channel_controls(self, hub: str, channel: str) -> dict[str, Any]:
        return self._request("GET", f"/hubs/{hub}/channels/{channel}/controls")

    def delete_channel_controls(self, hub: str, channel: str, body: dict | None = None) -> dict[str, Any]:
        return self._request("POST", f"/hubs/{hub}/channels/{channel}/controls_delete", json=body)

    def create_task_control(self, hub: str, channel: str, loc: str, task: str, body: dict | None = None) -> dict[str, Any]:
        return self._request("POST", f"/hubs/{hub}/channels/{channel}/locs/{loc}/tasks/{task}/controls", json=body)


class AsyncControlMixin:
    async def get_channel_controls(self, hub: str, channel: str) -> dict[str, Any]:
        return await self._request("GET", f"/hubs/{hub}/channels/{channel}/controls")

    async def delete_channel_controls(self, hub: str, channel: str, body: dict | None = None) -> dict[str, Any]:
        return await self._request("POST", f"/hubs/{hub}/channels/{channel}/controls_delete", json=body)

    async def create_task_control(self, hub: str, channel: str, loc: str, task: str, body: dict | None = None) -> dict[str, Any]:
        return await self._request("POST", f"/hubs/{hub}/channels/{channel}/locs/{loc}/tasks/{task}/controls", json=body)
