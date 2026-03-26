"""License interface."""

from __future__ import annotations

from typing import Any


class LicenseMixin:
    def list_licenses(self) -> dict[str, Any]:
        return self._request("GET", "/licenses")

    def get_license(self, license: str) -> dict[str, Any]:
        return self._request("GET", f"/licenses/{license}")

    def get_licensing(self) -> dict[str, Any]:
        return self._request("GET", "/licensing")

    def add_license(self, body: dict | None = None) -> dict[str, Any]:
        return self._request("POST", "/licenses", json=body)

    def accept_license_agreement(self, body: dict | None = None) -> dict[str, Any]:
        return self._request("POST", "/licensing/license_agreement_accepted", json=body)

    def delete_license(self, license: str) -> dict[str, Any]:
        return self._request("DELETE", f"/licenses/{license}")


class AsyncLicenseMixin:
    async def list_licenses(self) -> dict[str, Any]:
        return await self._request("GET", "/licenses")

    async def get_license(self, license: str) -> dict[str, Any]:
        return await self._request("GET", f"/licenses/{license}")

    async def get_licensing(self) -> dict[str, Any]:
        return await self._request("GET", "/licensing")

    async def add_license(self, body: dict | None = None) -> dict[str, Any]:
        return await self._request("POST", "/licenses", json=body)

    async def accept_license_agreement(self, body: dict | None = None) -> dict[str, Any]:
        return await self._request("POST", "/licensing/license_agreement_accepted", json=body)

    async def delete_license(self, license: str) -> dict[str, Any]:
        return await self._request("DELETE", f"/licenses/{license}")
