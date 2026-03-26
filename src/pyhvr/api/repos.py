"""Repository Config interface."""

from __future__ import annotations

from typing import Any


class RepoMixin:
    def get_repos(self) -> dict[str, Any]:
        return self._request("GET", "/repos")

    def get_repo_props(self) -> dict[str, Any]:
        return self._request("GET", "/repos/props")

    def create_repo(self, body: dict | None = None) -> dict[str, Any]:
        return self._request("POST", "/repos", json=body)

    def delete_repo_props(self, body: dict | None = None) -> dict[str, Any]:
        return self._request("POST", "/repos/props_delete", json=body)

    def patch_repo_props(self, body: dict | None = None) -> dict[str, Any]:
        return self._request("PATCH", "/repos/props", json=body)

    def put_repo_props(self, body: dict | None = None) -> dict[str, Any]:
        return self._request("PUT", "/repos/props", json=body)

    def delete_repo(self) -> dict[str, Any]:
        return self._request("DELETE", "/repos")


class AsyncRepoMixin:
    async def get_repos(self) -> dict[str, Any]:
        return await self._request("GET", "/repos")

    async def get_repo_props(self) -> dict[str, Any]:
        return await self._request("GET", "/repos/props")

    async def create_repo(self, body: dict | None = None) -> dict[str, Any]:
        return await self._request("POST", "/repos", json=body)

    async def delete_repo_props(self, body: dict | None = None) -> dict[str, Any]:
        return await self._request("POST", "/repos/props_delete", json=body)

    async def patch_repo_props(self, body: dict | None = None) -> dict[str, Any]:
        return await self._request("PATCH", "/repos/props", json=body)

    async def put_repo_props(self, body: dict | None = None) -> dict[str, Any]:
        return await self._request("PUT", "/repos/props", json=body)

    async def delete_repo(self) -> dict[str, Any]:
        return await self._request("DELETE", "/repos")
