"""Alert interface."""

from __future__ import annotations

from typing import Any


class AlertMixin:
    def list_alerts(self, hub: str) -> dict[str, Any]:
        return self._request("GET", f"/hubs/{hub}/alerts")

    def get_alert_props(self, hub: str, alert: str) -> dict[str, Any]:
        return self._request("GET", f"/hubs/{hub}/alerts/{alert}/props")

    def create_alert(self, hub: str, body: dict | None = None) -> dict[str, Any]:
        return self._request("POST", f"/hubs/{hub}/alerts", json=body)

    def clear_alert(self, hub: str, alert: str, body: dict | None = None) -> dict[str, Any]:
        return self._request("POST", f"/hubs/{hub}/alerts/{alert}/clear", json=body)

    def disable_alert(self, hub: str, alert: str, body: dict | None = None) -> dict[str, Any]:
        return self._request("POST", f"/hubs/{hub}/alerts/{alert}/disable", json=body)

    def execute_alert(self, hub: str, alert: str, body: dict | None = None) -> dict[str, Any]:
        return self._request("POST", f"/hubs/{hub}/alerts/{alert}/execute", json=body)

    def delete_alert_props(self, hub: str, alert: str, body: dict | None = None) -> dict[str, Any]:
        return self._request("POST", f"/hubs/{hub}/alerts/{alert}/props_delete", json=body)

    def test_alert(self, hub: str, alert: str, body: dict | None = None) -> dict[str, Any]:
        return self._request("POST", f"/hubs/{hub}/alerts/{alert}/test", json=body)

    def patch_alert_props(self, hub: str, alert: str, body: dict | None = None) -> dict[str, Any]:
        return self._request("PATCH", f"/hubs/{hub}/alerts/{alert}/props", json=body)

    def put_alert_props(self, hub: str, alert: str, body: dict | None = None) -> dict[str, Any]:
        return self._request("PUT", f"/hubs/{hub}/alerts/{alert}/props", json=body)

    def delete_alert(self, hub: str, alert: str) -> dict[str, Any]:
        return self._request("DELETE", f"/hubs/{hub}/alerts/{alert}")


class AsyncAlertMixin:
    async def list_alerts(self, hub: str) -> dict[str, Any]:
        return await self._request("GET", f"/hubs/{hub}/alerts")

    async def get_alert_props(self, hub: str, alert: str) -> dict[str, Any]:
        return await self._request("GET", f"/hubs/{hub}/alerts/{alert}/props")

    async def create_alert(self, hub: str, body: dict | None = None) -> dict[str, Any]:
        return await self._request("POST", f"/hubs/{hub}/alerts", json=body)

    async def clear_alert(self, hub: str, alert: str, body: dict | None = None) -> dict[str, Any]:
        return await self._request("POST", f"/hubs/{hub}/alerts/{alert}/clear", json=body)

    async def disable_alert(self, hub: str, alert: str, body: dict | None = None) -> dict[str, Any]:
        return await self._request("POST", f"/hubs/{hub}/alerts/{alert}/disable", json=body)

    async def execute_alert(self, hub: str, alert: str, body: dict | None = None) -> dict[str, Any]:
        return await self._request("POST", f"/hubs/{hub}/alerts/{alert}/execute", json=body)

    async def delete_alert_props(self, hub: str, alert: str, body: dict | None = None) -> dict[str, Any]:
        return await self._request("POST", f"/hubs/{hub}/alerts/{alert}/props_delete", json=body)

    async def test_alert(self, hub: str, alert: str, body: dict | None = None) -> dict[str, Any]:
        return await self._request("POST", f"/hubs/{hub}/alerts/{alert}/test", json=body)

    async def patch_alert_props(self, hub: str, alert: str, body: dict | None = None) -> dict[str, Any]:
        return await self._request("PATCH", f"/hubs/{hub}/alerts/{alert}/props", json=body)

    async def put_alert_props(self, hub: str, alert: str, body: dict | None = None) -> dict[str, Any]:
        return await self._request("PUT", f"/hubs/{hub}/alerts/{alert}/props", json=body)

    async def delete_alert(self, hub: str, alert: str) -> dict[str, Any]:
        return await self._request("DELETE", f"/hubs/{hub}/alerts/{alert}")
