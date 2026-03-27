"""Core HTTP client with sync and async implementations."""

from __future__ import annotations

import time
from typing import Any

import httpx

from pyhvr.api.activate import ActivateMixin, AsyncActivateMixin
from pyhvr.api.agent import AgentMixin, AsyncAgentMixin
from pyhvr.api.alerts import AlertMixin, AsyncAlertMixin
from pyhvr.api.controls import AsyncControlMixin, ControlMixin
from pyhvr.api.definition import AsyncDefinitionMixin, DefinitionMixin
from pyhvr.api.encryption import AsyncEncryptionMixin, EncryptionMixin
from pyhvr.api.events import AsyncEventMixin, EventMixin
from pyhvr.api.file_browse import AsyncFileBrowseMixin, FileBrowseMixin
from pyhvr.api.hubs import AsyncHubMixin, HubMixin
from pyhvr.api.hubserver import AsyncHubServerMixin, HubServerMixin
from pyhvr.api.jobs import AsyncJobMixin, JobMixin
from pyhvr.api.licenses import AsyncLicenseMixin, LicenseMixin
from pyhvr.api.logs import AsyncLogMixin, LogMixin
from pyhvr.api.metering import AsyncMeteringMixin, MeteringMixin
from pyhvr.api.misc import AsyncMiscMixin, MiscMixin
from pyhvr.api.query import AsyncQueryMixin, QueryMixin
from pyhvr.api.repos import AsyncRepoMixin, RepoMixin
from pyhvr.api.stats import AsyncStatsMixin, StatsMixin
from pyhvr.api.table_adapt import AsyncTableAdaptMixin, TableAdaptMixin
from pyhvr.api.users import AsyncUserMixin, UserMixin
from pyhvr.exceptions import ConnectionError, LoginError, RestError

# Tokens expire after 15 minutes; refresh 60 seconds early.
_TOKEN_REFRESH_BUFFER = 60


def _raise_for_response(response: httpx.Response) -> None:
    if response.is_error:
        try:
            message = response.json().get("message", response.text)
        except Exception:
            message = response.text
        raise RestError(response.status_code, message)


class HvrClient(
    ActivateMixin,
    AgentMixin,
    AlertMixin,
    ControlMixin,
    DefinitionMixin,
    EncryptionMixin,
    EventMixin,
    FileBrowseMixin,
    HubMixin,
    HubServerMixin,
    JobMixin,
    LicenseMixin,
    LogMixin,
    MeteringMixin,
    MiscMixin,
    QueryMixin,
    RepoMixin,
    StatsMixin,
    TableAdaptMixin,
    UserMixin,
):
    """Synchronous HVR REST API client."""

    def __init__(
        self,
        base_url: str,
        username: str,
        password: str,
        api_version: str = "latest",
    ) -> None:
        self._base_url = base_url.rstrip("/")
        self._username = username
        self._password = password
        self._api_version = api_version
        self._access_token: str | None = None
        self._refresh_token: str | None = None
        self._token_expires_at: float = 0.0

        import ssl
        ssl_context = ssl.create_default_context()
        self._http = httpx.Client(verify=ssl_context)

    def __enter__(self) -> HvrClient:
        self._login()
        return self

    def __exit__(self, *_: object) -> None:
        self._http.close()

    def _login(self) -> None:
        url = f"{self._base_url}/auth/v1/password"
        try:
            response = self._http.post(
                url,
                json={"username": self._username, "password": self._password, "refresh": "token"},
            )
        except httpx.ConnectError as exc:
            raise ConnectionError(f"Cannot connect to {self._base_url}: {exc}") from exc
        if response.is_error:
            raise LoginError(f"Login failed (HTTP {response.status_code}): {response.text}")
        data = response.json()
        self._access_token = data["access_token"]
        self._refresh_token = data.get("refresh_token")
        self._token_expires_at = time.monotonic() + data.get("expires_in", 900)

    def _ensure_token(self) -> None:
        if time.monotonic() >= self._token_expires_at - _TOKEN_REFRESH_BUFFER:
            if self._refresh_token:
                self._do_refresh()
            else:
                self._login()

    def _do_refresh(self) -> None:
        url = f"{self._base_url}/auth/v1/refresh"
        response = self._http.post(
            url,
            json={"refresh_token": self._refresh_token, "refresh": "token"},
        )
        if response.is_error:
            self._login()
            return
        data = response.json()
        self._access_token = data["access_token"]
        self._refresh_token = data.get("refresh_token", self._refresh_token)
        self._token_expires_at = time.monotonic() + data.get("expires_in", 900)

    def _request(self, method: str, path: str, **kwargs: Any) -> Any:
        self._ensure_token()
        url = f"{self._base_url}/api/{self._api_version}{path}"
        headers = {"Authorization": f"bearer {self._access_token}"}
        try:
            response = self._http.request(method, url, headers=headers, **kwargs)
        except httpx.ConnectError as exc:
            raise ConnectionError(f"Cannot connect to {self._base_url}: {exc}") from exc
        _raise_for_response(response)
        if response.content:
            try:
                return response.json()
            except Exception:
                return response.text
        return None


class AsyncHvrClient(
    AsyncActivateMixin,
    AsyncAgentMixin,
    AsyncAlertMixin,
    AsyncControlMixin,
    AsyncDefinitionMixin,
    AsyncEncryptionMixin,
    AsyncEventMixin,
    AsyncFileBrowseMixin,
    AsyncHubMixin,
    AsyncHubServerMixin,
    AsyncJobMixin,
    AsyncLicenseMixin,
    AsyncLogMixin,
    AsyncMeteringMixin,
    AsyncMiscMixin,
    AsyncQueryMixin,
    AsyncRepoMixin,
    AsyncStatsMixin,
    AsyncTableAdaptMixin,
    AsyncUserMixin,
):
    """Asynchronous HVR REST API client."""

    def __init__(
        self,
        base_url: str,
        username: str,
        password: str,
        api_version: str = "latest",
    ) -> None:
        self._base_url = base_url.rstrip("/")
        self._username = username
        self._password = password
        self._api_version = api_version
        self._access_token: str | None = None
        self._refresh_token: str | None = None
        self._token_expires_at: float = 0.0

        import ssl
        ssl_context = ssl.create_default_context()
        self._http = httpx.AsyncClient(verify=ssl_context)

    async def __aenter__(self) -> AsyncHvrClient:
        await self._login()
        return self

    async def __aexit__(self, *_: object) -> None:
        await self._http.aclose()

    async def _login(self) -> None:
        url = f"{self._base_url}/auth/v1/password"
        try:
            response = await self._http.post(
                url,
                json={"username": self._username, "password": self._password, "refresh": "token"},
            )
        except httpx.ConnectError as exc:
            raise ConnectionError(f"Cannot connect to {self._base_url}: {exc}") from exc
        if response.is_error:
            raise LoginError(f"Login failed (HTTP {response.status_code}): {response.text}")
        data = response.json()
        self._access_token = data["access_token"]
        self._refresh_token = data.get("refresh_token")
        self._token_expires_at = time.monotonic() + data.get("expires_in", 900)

    async def _ensure_token(self) -> None:
        if time.monotonic() >= self._token_expires_at - _TOKEN_REFRESH_BUFFER:
            if self._refresh_token:
                await self._do_refresh()
            else:
                await self._login()

    async def _do_refresh(self) -> None:
        url = f"{self._base_url}/auth/v1/refresh"
        response = await self._http.post(
            url,
            json={"refresh_token": self._refresh_token, "refresh": "token"},
        )
        if response.is_error:
            await self._login()
            return
        data = response.json()
        self._access_token = data["access_token"]
        self._refresh_token = data.get("refresh_token", self._refresh_token)
        self._token_expires_at = time.monotonic() + data.get("expires_in", 900)

    async def _request(self, method: str, path: str, **kwargs: Any) -> Any:
        await self._ensure_token()
        url = f"{self._base_url}/api/{self._api_version}{path}"
        headers = {"Authorization": f"bearer {self._access_token}"}
        try:
            response = await self._http.request(method, url, headers=headers, **kwargs)
        except httpx.ConnectError as exc:
            raise ConnectionError(f"Cannot connect to {self._base_url}: {exc}") from exc
        _raise_for_response(response)
        if response.content:
            try:
                return response.json()
            except Exception:
                return response.text
        return None
