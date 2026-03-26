"""User Config interface."""

from __future__ import annotations

from typing import Any


class UserMixin:
    def list_users(self) -> dict[str, Any]:
        return self._request("GET", "/users")

    def get_user(self, user: str) -> dict[str, Any]:
        return self._request("GET", f"/users/{user}")

    def get_user_props(self, user: str) -> dict[str, Any]:
        return self._request("GET", f"/users/{user}/props")

    def create_user(self, body: dict | None = None) -> dict[str, Any]:
        return self._request("POST", "/users", json=body)

    def delete_user_props(self, user: str, body: dict | None = None) -> dict[str, Any]:
        return self._request("POST", f"/users/{user}/props_delete", json=body)

    def patch_user_props(self, user: str, body: dict | None = None) -> dict[str, Any]:
        return self._request("PATCH", f"/users/{user}/props", json=body)

    def change_user_password(self, user: str, body: dict | None = None) -> dict[str, Any]:
        return self._request("PUT", f"/users/{user}/password", json=body)

    def put_user_props(self, user: str, body: dict | None = None) -> dict[str, Any]:
        return self._request("PUT", f"/users/{user}/props", json=body)

    def delete_user(self, user: str) -> dict[str, Any]:
        return self._request("DELETE", f"/users/{user}")


class AsyncUserMixin:
    async def list_users(self) -> dict[str, Any]:
        return await self._request("GET", "/users")

    async def get_user(self, user: str) -> dict[str, Any]:
        return await self._request("GET", f"/users/{user}")

    async def get_user_props(self, user: str) -> dict[str, Any]:
        return await self._request("GET", f"/users/{user}/props")

    async def create_user(self, body: dict | None = None) -> dict[str, Any]:
        return await self._request("POST", "/users", json=body)

    async def delete_user_props(self, user: str, body: dict | None = None) -> dict[str, Any]:
        return await self._request("POST", f"/users/{user}/props_delete", json=body)

    async def patch_user_props(self, user: str, body: dict | None = None) -> dict[str, Any]:
        return await self._request("PATCH", f"/users/{user}/props", json=body)

    async def change_user_password(self, user: str, body: dict | None = None) -> dict[str, Any]:
        return await self._request("PUT", f"/users/{user}/password", json=body)

    async def put_user_props(self, user: str, body: dict | None = None) -> dict[str, Any]:
        return await self._request("PUT", f"/users/{user}/props", json=body)

    async def delete_user(self, user: str) -> dict[str, Any]:
        return await self._request("DELETE", f"/users/{user}")
