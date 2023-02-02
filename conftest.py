import pytest
from modules.api.clients.github import GitHub
from modules.api.clients.users_data import User


@pytest.fixture
def user():
    user = User()
    user.create()

    yield user

    user.remove()


@pytest.fixture
def github_api():
    api = GitHub()

    yield api
