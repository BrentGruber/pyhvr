"""Hub Config interface."""

from __future__ import annotations

from typing import Any


class HubMixin:
    def list_hubs(self) -> dict[str, Any]:
        return self._request("GET", "/hubs")

    def get_hub(self, hub: str) -> dict[str, Any]:
        return self._request("GET", f"/hubs/{hub}")

    def get_hub_props(self, hub: str) -> dict[str, Any]:
        return self._request("GET", f"/hubs/{hub}/props")

    def get_hub_user_props(self, hub: str, user: str) -> dict[str, Any]:
        return self._request("GET", f"/hubs/{hub}/users/{user}/props")

    def create_hub(self, body: dict | None = None) -> dict[str, Any]:
        return self._request("POST", "/hubs", json=body)

    def delete_hub_props(self, hub: str, body: dict | None = None) -> dict[str, Any]:
        return self._request("POST", f"/hubs/{hub}/props_delete", json=body)

    def delete_hub_user_props(self, hub: str, user: str, body: dict | None = None) -> dict[str, Any]:
        return self._request("POST", f"/hubs/{hub}/users/{user}/props_delete", json=body)

    def freeze_hub(self, hub: str, body: dict | None = None) -> dict[str, Any]:
        return self._request("POST", f"/hubs/{hub}/freeze", json=body)

    def unfreeze_hub(self, hub: str, body: dict | None = None) -> dict[str, Any]:
        return self._request("POST", f"/hubs/{hub}/unfreeze", json=body)

    def snapshot_hub(self, hub: str, body: dict | None = None) -> dict[str, Any]:
        return self._request("POST", f"/hubs/{hub}/snapshot", json=body)

    def patch_hub_props(self, hub: str, body: dict | None = None) -> dict[str, Any]:
        return self._request("PATCH", f"/hubs/{hub}/props", json=body)

    def patch_hub_user_props(self, hub: str, user: str, body: dict | None = None) -> dict[str, Any]:
        return self._request("PATCH", f"/hubs/{hub}/users/{user}/props", json=body)

    def put_job_system_attributes(self, hub: str, body: dict | None = None) -> dict[str, Any]:
        return self._request("PUT", f"/hubs/{hub}/job_system/attributes", json=body)

    def delete_hub(self, hub: str) -> dict[str, Any]:
        return self._request("DELETE", f"/hubs/{hub}")


class AsyncHubMixin:
    async def list_hubs(self) -> dict[str, Any]:
        return await self._request("GET", "/hubs")

    async def get_hub(self, hub: str) -> dict[str, Any]:
        return await self._request("GET", f"/hubs/{hub}")

    async def get_hub_props(self, hub: str) -> dict[str, Any]:
        return await self._request("GET", f"/hubs/{hub}/props")

    async def get_hub_user_props(self, hub: str, user: str) -> dict[str, Any]:
        return await self._request("GET", f"/hubs/{hub}/users/{user}/props")

    async def create_hub(self, body: dict | None = None) -> dict[str, Any]:
        return await self._request("POST", "/hubs", json=body)

    async def delete_hub_props(self, hub: str, body: dict | None = None) -> dict[str, Any]:
        return await self._request("POST", f"/hubs/{hub}/props_delete", json=body)

    async def delete_hub_user_props(self, hub: str, user: str, body: dict | None = None) -> dict[str, Any]:
        return await self._request("POST", f"/hubs/{hub}/users/{user}/props_delete", json=body)

    async def freeze_hub(self, hub: str, body: dict | None = None) -> dict[str, Any]:
        return await self._request("POST", f"/hubs/{hub}/freeze", json=body)

    async def unfreeze_hub(self, hub: str, body: dict | None = None) -> dict[str, Any]:
        return await self._request("POST", f"/hubs/{hub}/unfreeze", json=body)

    async def snapshot_hub(self, hub: str, body: dict | None = None) -> dict[str, Any]:
        return await self._request("POST", f"/hubs/{hub}/snapshot", json=body)

    async def patch_hub_props(self, hub: str, body: dict | None = None) -> dict[str, Any]:
        return await self._request("PATCH", f"/hubs/{hub}/props", json=body)

    async def patch_hub_user_props(self, hub: str, user: str, body: dict | None = None) -> dict[str, Any]:
        return await self._request("PATCH", f"/hubs/{hub}/users/{user}/props", json=body)

    async def put_job_system_attributes(self, hub: str, body: dict | None = None) -> dict[str, Any]:
        return await self._request("PUT", f"/hubs/{hub}/job_system/attributes", json=body)

    async def delete_hub(self, hub: str) -> dict[str, Any]:
        return await self._request("DELETE", f"/hubs/{hub}")
