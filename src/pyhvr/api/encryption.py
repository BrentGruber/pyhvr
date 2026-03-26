"""Encryption (Wallet) interface."""

from __future__ import annotations

from typing import Any


class EncryptionMixin:
    def get_wallet_props(self) -> dict[str, Any]:
        return self._request("GET", "/wallet/props")

    def create_wallet(self, body: dict | None = None) -> dict[str, Any]:
        return self._request("POST", "/wallet", json=body)

    def change_wallet(self, body: dict | None = None) -> dict[str, Any]:
        return self._request("POST", "/wallet/change", json=body)

    def disable_wallet(self, body: dict | None = None) -> dict[str, Any]:
        return self._request("POST", "/wallet/disable", json=body)

    def delete_wallet_key_history(self, body: dict | None = None) -> dict[str, Any]:
        return self._request("POST", "/wallet/key_history_delete", json=body)

    def rotate_wallet_key(self, body: dict | None = None) -> dict[str, Any]:
        return self._request("POST", "/wallet/key_rotate", json=body)

    def migrate_wallet(self, body: dict | None = None) -> dict[str, Any]:
        return self._request("POST", "/wallet/migrate", json=body)

    def continue_reencrypt(self, body: dict | None = None) -> dict[str, Any]:
        return self._request("POST", "/wallet/reencrypt_continue", json=body)


class AsyncEncryptionMixin:
    async def get_wallet_props(self) -> dict[str, Any]:
        return await self._request("GET", "/wallet/props")

    async def create_wallet(self, body: dict | None = None) -> dict[str, Any]:
        return await self._request("POST", "/wallet", json=body)

    async def change_wallet(self, body: dict | None = None) -> dict[str, Any]:
        return await self._request("POST", "/wallet/change", json=body)

    async def disable_wallet(self, body: dict | None = None) -> dict[str, Any]:
        return await self._request("POST", "/wallet/disable", json=body)

    async def delete_wallet_key_history(self, body: dict | None = None) -> dict[str, Any]:
        return await self._request("POST", "/wallet/key_history_delete", json=body)

    async def rotate_wallet_key(self, body: dict | None = None) -> dict[str, Any]:
        return await self._request("POST", "/wallet/key_rotate", json=body)

    async def migrate_wallet(self, body: dict | None = None) -> dict[str, Any]:
        return await self._request("POST", "/wallet/migrate", json=body)

    async def continue_reencrypt(self, body: dict | None = None) -> dict[str, Any]:
        return await self._request("POST", "/wallet/reencrypt_continue", json=body)
