class PyhvrError(Exception):
    """Base exception for all pyhvr errors."""


class LoginError(PyhvrError):
    """Raised when authentication fails."""


class ConnectionError(PyhvrError):
    """Raised when the server cannot be reached."""


class RestError(PyhvrError):
    """Raised when the API returns a 4xx or 5xx response."""

    def __init__(self, status_code: int, message: str) -> None:
        self.status_code = status_code
        # HVR error codes are the first 8 chars: "F_JRxxxY"
        if len(message) > 8 and message[0] == "F" and message[1] == "_":
            self.error_code = message[:8]
            self.detail = message[9:].strip()
        else:
            self.error_code = None
            self.detail = message
        super().__init__(f"HTTP {status_code}: {message}")
