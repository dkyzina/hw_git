import pytest

@pytest.fixture
def browser():
    print("браузер!")
    pass

@pytest.fixture
def login_page(browser):
    print("логин пейдж!")
    pass

@pytest.fixture
def user():
    print("юзер!")
    return "username", "password"


def test_login(login_page, user):
    username, password = user
    assert username == "username"
    assert password == "password"