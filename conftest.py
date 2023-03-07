import pytest
from modules.api.clients.github import GitHub
from modules.api.clients.users_data import User
from modules.common.database import Database
from modules.ui.page_objects.sign_in_page import SignInPage


@pytest.fixture
def newUser():
    testUser = User()
    testUser.create()

    yield testUser

    testUser.remove()


@pytest.fixture
def github_api():
    api = GitHub()

    yield api


@pytest.fixture
def database_api():
    data = Database()

    yield data


@pytest.fixture
def sign_in_page_ui():
    sign_in_page = SignInPage()

    yield sign_in_page
