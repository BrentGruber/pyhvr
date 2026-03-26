"""Statistics interface."""

from __future__ import annotations

from typing import Any


class StatsMixin:
    def get_stats_metrics(self, hub: str) -> dict[str, Any]:
        return self._request("GET", f"/hubs/{hub}/stats/metrics")

    def export_stats_metrics(self, hub: str, body: dict | None = None) -> dict[str, Any]:
        return self._request("POST", f"/hubs/{hub}/stats/metrics_export", json=body)


class AsyncStatsMixin:
    async def get_stats_metrics(self, hub: str) -> dict[str, Any]:
        return await self._request("GET", f"/hubs/{hub}/stats/metrics")

    async def export_stats_metrics(self, hub: str, body: dict | None = None) -> dict[str, Any]:
        return await self._request("POST", f"/hubs/{hub}/stats/metrics_export", json=body)
