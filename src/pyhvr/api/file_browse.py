"""File and DB Browse interface."""

from __future__ import annotations

from typing import Any


class FileBrowseMixin:
    def browse_hub_dirs(self, hub: str) -> dict[str, Any]:
        return self._request("GET", f"/hubs/{hub}/dirs")

    def get_loc_db_schemas(self, hub: str, loc: str) -> dict[str, Any]:
        return self._request("GET", f"/hubs/{hub}/locs/{loc}/db_schemas")

    def browse_loc_dirs(self, hub: str, loc: str) -> dict[str, Any]:
        return self._request("GET", f"/hubs/{hub}/locs/{loc}/dirs")

    def get_loc_odbc_drivers(self, hub: str, loc: str) -> dict[str, Any]:
        return self._request("GET", f"/hubs/{hub}/locs/{loc}/env/odbc_drivers")

    def get_loc_oratab(self, hub: str, loc: str) -> dict[str, Any]:
        return self._request("GET", f"/hubs/{hub}/locs/{loc}/env/oratab")

    def get_loc_env_vars(self, hub: str, loc: str) -> dict[str, Any]:
        return self._request("GET", f"/hubs/{hub}/locs/{loc}/env/vars")

    def test_loc_connection(self, hub: str, loc: str, body: dict | None = None) -> dict[str, Any]:
        return self._request("POST", f"/hubs/{hub}/locs/{loc}/test", json=body)

    def get_new_loc_db_schemas(self, hub: str, body: dict | None = None) -> dict[str, Any]:
        return self._request("POST", f"/hubs/{hub}/new_loc/db_schemas", json=body)

    def browse_new_loc_dirs(self, hub: str, body: dict | None = None) -> dict[str, Any]:
        return self._request("POST", f"/hubs/{hub}/new_loc/dirs", json=body)

    def get_new_loc_odbc_drivers(self, hub: str, body: dict | None = None) -> dict[str, Any]:
        return self._request("POST", f"/hubs/{hub}/new_loc/env/odbc_drivers", json=body)

    def get_new_loc_oratab(self, hub: str, body: dict | None = None) -> dict[str, Any]:
        return self._request("POST", f"/hubs/{hub}/new_loc/env/oratab", json=body)

    def get_new_loc_env_vars(self, hub: str, body: dict | None = None) -> dict[str, Any]:
        return self._request("POST", f"/hubs/{hub}/new_loc/env/vars", json=body)

    def test_new_loc_connection(self, hub: str, body: dict | None = None) -> dict[str, Any]:
        return self._request("POST", f"/hubs/{hub}/new_loc/test", json=body)


class AsyncFileBrowseMixin:
    async def browse_hub_dirs(self, hub: str) -> dict[str, Any]:
        return await self._request("GET", f"/hubs/{hub}/dirs")

    async def get_loc_db_schemas(self, hub: str, loc: str) -> dict[str, Any]:
        return await self._request("GET", f"/hubs/{hub}/locs/{loc}/db_schemas")

    async def browse_loc_dirs(self, hub: str, loc: str) -> dict[str, Any]:
        return await self._request("GET", f"/hubs/{hub}/locs/{loc}/dirs")

    async def get_loc_odbc_drivers(self, hub: str, loc: str) -> dict[str, Any]:
        return await self._request("GET", f"/hubs/{hub}/locs/{loc}/env/odbc_drivers")

    async def get_loc_oratab(self, hub: str, loc: str) -> dict[str, Any]:
        return await self._request("GET", f"/hubs/{hub}/locs/{loc}/env/oratab")

    async def get_loc_env_vars(self, hub: str, loc: str) -> dict[str, Any]:
        return await self._request("GET", f"/hubs/{hub}/locs/{loc}/env/vars")

    async def test_loc_connection(self, hub: str, loc: str, body: dict | None = None) -> dict[str, Any]:
        return await self._request("POST", f"/hubs/{hub}/locs/{loc}/test", json=body)

    async def get_new_loc_db_schemas(self, hub: str, body: dict | None = None) -> dict[str, Any]:
        return await self._request("POST", f"/hubs/{hub}/new_loc/db_schemas", json=body)

    async def browse_new_loc_dirs(self, hub: str, body: dict | None = None) -> dict[str, Any]:
        return await self._request("POST", f"/hubs/{hub}/new_loc/dirs", json=body)

    async def get_new_loc_odbc_drivers(self, hub: str, body: dict | None = None) -> dict[str, Any]:
        return await self._request("POST", f"/hubs/{hub}/new_loc/env/odbc_drivers", json=body)

    async def get_new_loc_oratab(self, hub: str, body: dict | None = None) -> dict[str, Any]:
        return await self._request("POST", f"/hubs/{hub}/new_loc/env/oratab", json=body)

    async def get_new_loc_env_vars(self, hub: str, body: dict | None = None) -> dict[str, Any]:
        return await self._request("POST", f"/hubs/{hub}/new_loc/env/vars", json=body)

    async def test_new_loc_connection(self, hub: str, body: dict | None = None) -> dict[str, Any]:
        return await self._request("POST", f"/hubs/{hub}/new_loc/test", json=body)
