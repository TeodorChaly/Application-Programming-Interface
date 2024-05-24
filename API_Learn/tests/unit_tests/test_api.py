# tests/unit_tests/test_api.py
import pytest
from httpx import Client


@pytest.fixture
def ac():
    return Client()


@pytest.mark.parametrize("email, password, status_code", [
    ("test_user@gmail.com", "test_password", 200),
    ("test_no_gmail", "test_password", 422)
])
def test_register_user(email, password, status_code, ac: Client):
    response = ac.post("http://127.0.0.1:80/auth/register", json={
        "email": email,
        "password": password
    })
    assert response.status_code == status_code


@pytest.mark.parametrize("email, password, status_code", [
    ("user@example.com", "123", 200),
    ("user_not_exist@example.com", "123", 401)
])
def test_login_user(email, password, status_code, ac: Client):
    response = ac.post("http://127.0.0.1:80/auth/login", json={
        "email": email,
        "password": password
    })
    assert response.status_code == status_code

# pytest -v -s
# -v - to see the output of the tests
# -s - to see the print statements
