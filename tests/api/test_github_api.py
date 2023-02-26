import pytest


@pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_user("defunkt")

    assert user["login"] == "defunkt"


@pytest.mark.api
def test_user_not_exists(github_api):
    m = github_api.get_user("MudrykYurii")

    assert m["message"] == "Not Found"


@pytest.mark.api
def test_repo_can_be_found(github_api):
    r = github_api.search_repo("become-qa-auto")

    assert r["total_count"] == 32


@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    r = github_api.search_repo("MudrykYurii_repo_non_exist")

    assert r["total_count"] == 0
