"""Logfile Tailing interface."""

from __future__ import annotations

from typing import Any


class LogMixin:
    def get_log(self, file: str) -> Any:
        return self._request("GET", f"/logs/{file}")

    def get_log_archive(self, file: str, archive: str) -> Any:
        return self._request("GET", f"/logs/{file}/archive/{archive}")

    def get_hub_log(self, hub: str, file: str) -> Any:
        return self._request("GET", f"/hubs/{hub}/logs/{file}")

    def get_hub_log_archive(self, hub: str, file: str, archive: str) -> Any:
        return self._request("GET", f"/hubs/{hub}/logs/{file}/archive/{archive}")

    def search_hub_log(self, hub: str, file: str) -> Any:
        return self._request("GET", f"/hubs/{hub}/logs/{file}/search")


class AsyncLogMixin:
    async def get_log(self, file: str) -> Any:
        return await self._request("GET", f"/logs/{file}")

    async def get_log_archive(self, file: str, archive: str) -> Any:
        return await self._request("GET", f"/logs/{file}/archive/{archive}")

    async def get_hub_log(self, hub: str, file: str) -> Any:
        return await self._request("GET", f"/hubs/{hub}/logs/{file}")

    async def get_hub_log_archive(self, hub: str, file: str, archive: str) -> Any:
        return await self._request("GET", f"/hubs/{hub}/logs/{file}/archive/{archive}")

    async def search_hub_log(self, hub: str, file: str) -> Any:
        return await self._request("GET", f"/hubs/{hub}/logs/{file}/search")
