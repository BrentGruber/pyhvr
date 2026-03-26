"""Metering interface."""

from __future__ import annotations

from typing import Any


class MeteringMixin:
    def download_metering(self) -> dict[str, Any]:
        return self._request("GET", "/metering/download")

    def acquire_metering_license(self, body: dict | None = None) -> dict[str, Any]:
        return self._request("POST", "/metering/license_acquire", json=body)

    def purge_metering(self, body: dict | None = None) -> dict[str, Any]:
        return self._request("POST", "/metering/purge", json=body)

    def get_metering_registration_status(self, body: dict | None = None) -> dict[str, Any]:
        return self._request("POST", "/metering/registration_status", json=body)

    def upload_metering(self, body: dict | None = None) -> dict[str, Any]:
        return self._request("POST", "/metering/upload", json=body)


class AsyncMeteringMixin:
    async def download_metering(self) -> dict[str, Any]:
        return await self._request("GET", "/metering/download")

    async def acquire_metering_license(self, body: dict | None = None) -> dict[str, Any]:
        return await self._request("POST", "/metering/license_acquire", json=body)

    async def purge_metering(self, body: dict | None = None) -> dict[str, Any]:
        return await self._request("POST", "/metering/purge", json=body)

    async def get_metering_registration_status(self, body: dict | None = None) -> dict[str, Any]:
        return await self._request("POST", "/metering/registration_status", json=body)

    async def upload_metering(self, body: dict | None = None) -> dict[str, Any]:
        return await self._request("POST", "/metering/upload", json=body)
