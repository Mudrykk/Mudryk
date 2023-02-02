import pytest


@pytest.mark.http
def test_first_request(github_api):
    m = github_api.send_first_request()
    print(f"{m.text}")


@pytest.mark.http
def test_second_request(github_api):
    r = github_api.get_user("defunkt")
    s = github_api.get_status_code("defunkt")
    h = github_api.get_headers("defunkt")

    assert r["name"] == "Chris Wanstrath"
    assert s == 200
    assert h["Server"] == "GitHub.com"


@pytest.mark.http
def test_status_code_request(github_api):
    r = github_api.get_status_code("MudrykYurii")

    assert r == 404
