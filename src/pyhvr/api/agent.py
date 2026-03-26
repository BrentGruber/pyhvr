"""Agent Configuration interface."""

from __future__ import annotations

from typing import Any


class AgentMixin:
    def get_loc_agent(self, hub: str, loc: str) -> dict[str, Any]:
        return self._request("GET", f"/hubs/{hub}/locs/{loc}/agent")

    def delete_agent_props(self, hub: str, loc: str, body: dict | None = None) -> dict[str, Any]:
        return self._request("POST", f"/hubs/{hub}/locs/{loc}/agent/props_delete", json=body)

    def get_agent_props(self, hub: str, loc: str, body: dict | None = None) -> dict[str, Any]:
        return self._request("POST", f"/hubs/{hub}/locs/{loc}/agent/props_get", json=body)

    def patch_agent_props(self, hub: str, loc: str, body: dict | None = None) -> dict[str, Any]:
        return self._request("POST", f"/hubs/{hub}/locs/{loc}/agent/props_patch", json=body)

    def put_agent_props(self, hub: str, loc: str, body: dict | None = None) -> dict[str, Any]:
        return self._request("POST", f"/hubs/{hub}/locs/{loc}/agent/props_put", json=body)

    def test_agent(self, hub: str, loc: str, body: dict | None = None) -> dict[str, Any]:
        return self._request("POST", f"/hubs/{hub}/locs/{loc}/agent/test", json=body)

    def create_agent_user(self, hub: str, loc: str, body: dict | None = None) -> dict[str, Any]:
        return self._request("POST", f"/hubs/{hub}/locs/{loc}/agent/users", json=body)

    def delete_agent_user(self, hub: str, loc: str, body: dict | None = None) -> dict[str, Any]:
        return self._request("POST", f"/hubs/{hub}/locs/{loc}/agent/users_delete", json=body)

    def get_agent_users(self, hub: str, loc: str, body: dict | None = None) -> dict[str, Any]:
        return self._request("POST", f"/hubs/{hub}/locs/{loc}/agent/users_get", json=body)

    def change_agent_user_password(self, hub: str, loc: str, body: dict | None = None) -> dict[str, Any]:
        return self._request("POST", f"/hubs/{hub}/locs/{loc}/agent/users_password", json=body)

    def test_new_loc_agent(self, hub: str, body: dict | None = None) -> dict[str, Any]:
        return self._request("POST", f"/hubs/{hub}/new_loc/agent/test", json=body)

    def get_new_loc_agent(self, hub: str, body: dict | None = None) -> dict[str, Any]:
        return self._request("POST", f"/hubs/{hub}/new_loc/agent/get", json=body)

    def delete_new_loc_agent_props(self, hub: str, body: dict | None = None) -> dict[str, Any]:
        return self._request("POST", f"/hubs/{hub}/new_loc/agent/props_delete", json=body)

    def get_new_loc_agent_props(self, hub: str, body: dict | None = None) -> dict[str, Any]:
        return self._request("POST", f"/hubs/{hub}/new_loc/agent/props_get", json=body)

    def patch_new_loc_agent_props(self, hub: str, body: dict | None = None) -> dict[str, Any]:
        return self._request("POST", f"/hubs/{hub}/new_loc/agent/props_patch", json=body)

    def put_new_loc_agent_props(self, hub: str, body: dict | None = None) -> dict[str, Any]:
        return self._request("POST", f"/hubs/{hub}/new_loc/agent/props_put", json=body)

    def create_new_loc_agent_user(self, hub: str, body: dict | None = None) -> dict[str, Any]:
        return self._request("POST", f"/hubs/{hub}/new_loc/agent/users", json=body)

    def delete_new_loc_agent_user(self, hub: str, body: dict | None = None) -> dict[str, Any]:
        return self._request("POST", f"/hubs/{hub}/new_loc/agent/users_delete", json=body)

    def get_new_loc_agent_users(self, hub: str, body: dict | None = None) -> dict[str, Any]:
        return self._request("POST", f"/hubs/{hub}/new_loc/agent/users_get", json=body)

    def change_new_loc_agent_user_password(self, hub: str, body: dict | None = None) -> dict[str, Any]:
        return self._request("POST", f"/hubs/{hub}/new_loc/agent/users_password", json=body)


class AsyncAgentMixin:
    async def get_loc_agent(self, hub: str, loc: str) -> dict[str, Any]:
        return await self._request("GET", f"/hubs/{hub}/locs/{loc}/agent")

    async def delete_agent_props(self, hub: str, loc: str, body: dict | None = None) -> dict[str, Any]:
        return await self._request("POST", f"/hubs/{hub}/locs/{loc}/agent/props_delete", json=body)

    async def get_agent_props(self, hub: str, loc: str, body: dict | None = None) -> dict[str, Any]:
        return await self._request("POST", f"/hubs/{hub}/locs/{loc}/agent/props_get", json=body)

    async def patch_agent_props(self, hub: str, loc: str, body: dict | None = None) -> dict[str, Any]:
        return await self._request("POST", f"/hubs/{hub}/locs/{loc}/agent/props_patch", json=body)

    async def put_agent_props(self, hub: str, loc: str, body: dict | None = None) -> dict[str, Any]:
        return await self._request("POST", f"/hubs/{hub}/locs/{loc}/agent/props_put", json=body)

    async def test_agent(self, hub: str, loc: str, body: dict | None = None) -> dict[str, Any]:
        return await self._request("POST", f"/hubs/{hub}/locs/{loc}/agent/test", json=body)

    async def create_agent_user(self, hub: str, loc: str, body: dict | None = None) -> dict[str, Any]:
        return await self._request("POST", f"/hubs/{hub}/locs/{loc}/agent/users", json=body)

    async def delete_agent_user(self, hub: str, loc: str, body: dict | None = None) -> dict[str, Any]:
        return await self._request("POST", f"/hubs/{hub}/locs/{loc}/agent/users_delete", json=body)

    async def get_agent_users(self, hub: str, loc: str, body: dict | None = None) -> dict[str, Any]:
        return await self._request("POST", f"/hubs/{hub}/locs/{loc}/agent/users_get", json=body)

    async def change_agent_user_password(self, hub: str, loc: str, body: dict | None = None) -> dict[str, Any]:
        return await self._request("POST", f"/hubs/{hub}/locs/{loc}/agent/users_password", json=body)

    async def test_new_loc_agent(self, hub: str, body: dict | None = None) -> dict[str, Any]:
        return await self._request("POST", f"/hubs/{hub}/new_loc/agent/test", json=body)

    async def get_new_loc_agent(self, hub: str, body: dict | None = None) -> dict[str, Any]:
        return await self._request("POST", f"/hubs/{hub}/new_loc/agent/get", json=body)

    async def delete_new_loc_agent_props(self, hub: str, body: dict | None = None) -> dict[str, Any]:
        return await self._request("POST", f"/hubs/{hub}/new_loc/agent/props_delete", json=body)

    async def get_new_loc_agent_props(self, hub: str, body: dict | None = None) -> dict[str, Any]:
        return await self._request("POST", f"/hubs/{hub}/new_loc/agent/props_get", json=body)

    async def patch_new_loc_agent_props(self, hub: str, body: dict | None = None) -> dict[str, Any]:
        return await self._request("POST", f"/hubs/{hub}/new_loc/agent/props_patch", json=body)

    async def put_new_loc_agent_props(self, hub: str, body: dict | None = None) -> dict[str, Any]:
        return await self._request("POST", f"/hubs/{hub}/new_loc/agent/props_put", json=body)

    async def create_new_loc_agent_user(self, hub: str, body: dict | None = None) -> dict[str, Any]:
        return await self._request("POST", f"/hubs/{hub}/new_loc/agent/users", json=body)

    async def delete_new_loc_agent_user(self, hub: str, body: dict | None = None) -> dict[str, Any]:
        return await self._request("POST", f"/hubs/{hub}/new_loc/agent/users_delete", json=body)

    async def get_new_loc_agent_users(self, hub: str, body: dict | None = None) -> dict[str, Any]:
        return await self._request("POST", f"/hubs/{hub}/new_loc/agent/users_get", json=body)

    async def change_new_loc_agent_user_password(self, hub: str, body: dict | None = None) -> dict[str, Any]:
        return await self._request("POST", f"/hubs/{hub}/new_loc/agent/users_password", json=body)
