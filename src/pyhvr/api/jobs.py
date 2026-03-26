"""Job interface."""

from __future__ import annotations

from typing import Any


class JobMixin:
    def list_jobs(self, hub: str) -> dict[str, Any]:
        return self._request("GET", f"/hubs/{hub}/jobs")

    def get_job_attributes(self, hub: str, job: str) -> dict[str, Any]:
        return self._request("GET", f"/hubs/{hub}/jobs/{job}/attributes")

    def get_job_control_log(self, hub: str, job: str) -> dict[str, Any]:
        return self._request("GET", f"/hubs/{hub}/jobs/{job}/controls/log")

    def get_job_env_vars(self, hub: str, job: str) -> dict[str, Any]:
        return self._request("GET", f"/hubs/{hub}/jobs/{job}/env_vars")

    def get_job_system_attributes(self, hub: str) -> dict[str, Any]:
        return self._request("GET", f"/hubs/{hub}/job_system/attributes")

    def get_job_system_env_vars(self, hub: str) -> dict[str, Any]:
        return self._request("GET", f"/hubs/{hub}/job_system/env_vars")

    def delete_jobs(self, hub: str, body: dict | None = None) -> dict[str, Any]:
        return self._request("POST", f"/hubs/{hub}/jobs_delete", json=body)

    def start_jobs(self, hub: str, body: dict | None = None) -> dict[str, Any]:
        return self._request("POST", f"/hubs/{hub}/jobs_start", json=body)

    def suspend_jobs(self, hub: str, body: dict | None = None) -> dict[str, Any]:
        return self._request("POST", f"/hubs/{hub}/jobs_suspend", json=body)

    def unsuspend_jobs(self, hub: str, body: dict | None = None) -> dict[str, Any]:
        return self._request("POST", f"/hubs/{hub}/jobs_unsuspend", json=body)

    def put_job_env_vars(self, hub: str, job: str, body: dict | None = None) -> dict[str, Any]:
        return self._request("PUT", f"/hubs/{hub}/jobs/{job}/env_vars", json=body)

    def put_job_system_env_vars(self, hub: str, body: dict | None = None) -> dict[str, Any]:
        return self._request("PUT", f"/hubs/{hub}/job_system/env_vars", json=body)

    def delete_job_env_var(self, hub: str, job: str, var: str) -> dict[str, Any]:
        return self._request("DELETE", f"/hubs/{hub}/jobs/{job}/env_vars/{var}")


class AsyncJobMixin:
    async def list_jobs(self, hub: str) -> dict[str, Any]:
        return await self._request("GET", f"/hubs/{hub}/jobs")

    async def get_job_attributes(self, hub: str, job: str) -> dict[str, Any]:
        return await self._request("GET", f"/hubs/{hub}/jobs/{job}/attributes")

    async def get_job_control_log(self, hub: str, job: str) -> dict[str, Any]:
        return await self._request("GET", f"/hubs/{hub}/jobs/{job}/controls/log")

    async def get_job_env_vars(self, hub: str, job: str) -> dict[str, Any]:
        return await self._request("GET", f"/hubs/{hub}/jobs/{job}/env_vars")

    async def get_job_system_attributes(self, hub: str) -> dict[str, Any]:
        return await self._request("GET", f"/hubs/{hub}/job_system/attributes")

    async def get_job_system_env_vars(self, hub: str) -> dict[str, Any]:
        return await self._request("GET", f"/hubs/{hub}/job_system/env_vars")

    async def delete_jobs(self, hub: str, body: dict | None = None) -> dict[str, Any]:
        return await self._request("POST", f"/hubs/{hub}/jobs_delete", json=body)

    async def start_jobs(self, hub: str, body: dict | None = None) -> dict[str, Any]:
        return await self._request("POST", f"/hubs/{hub}/jobs_start", json=body)

    async def suspend_jobs(self, hub: str, body: dict | None = None) -> dict[str, Any]:
        return await self._request("POST", f"/hubs/{hub}/jobs_suspend", json=body)

    async def unsuspend_jobs(self, hub: str, body: dict | None = None) -> dict[str, Any]:
        return await self._request("POST", f"/hubs/{hub}/jobs_unsuspend", json=body)

    async def put_job_env_vars(self, hub: str, job: str, body: dict | None = None) -> dict[str, Any]:
        return await self._request("PUT", f"/hubs/{hub}/jobs/{job}/env_vars", json=body)

    async def put_job_system_env_vars(self, hub: str, body: dict | None = None) -> dict[str, Any]:
        return await self._request("PUT", f"/hubs/{hub}/job_system/env_vars", json=body)

    async def delete_job_env_var(self, hub: str, job: str, var: str) -> dict[str, Any]:
        return await self._request("DELETE", f"/hubs/{hub}/jobs/{job}/env_vars/{var}")
