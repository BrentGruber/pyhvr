"""Tests for exception parsing."""


from pyhvr.exceptions import ConnectionError, LoginError, PyhvrError, RestError


def test_rest_error_parses_hvr_error_code():
    err = RestError(400, "F_JR0001Y something went wrong")
    assert err.error_code == "F_JR0001"
    assert err.detail == "something went wrong"
    assert err.status_code == 400
    assert "HTTP 400" in str(err)


def test_rest_error_no_code():
    err = RestError(500, "Internal Server Error")
    assert err.error_code is None
    assert err.detail == "Internal Server Error"


def test_rest_error_is_pyhvr_error():
    assert issubclass(RestError, PyhvrError)


def test_login_error_is_pyhvr_error():
    assert issubclass(LoginError, PyhvrError)


def test_connection_error_is_pyhvr_error():
    assert issubclass(ConnectionError, PyhvrError)
