import pytest


@pytest.mark.ui
def test_check_username_page_object(sign_in_page_ui):
    sign_in_page_ui.go_to('https://github.com/login')

    sign_in_page_ui.try_login("unknown_user@gmail.com", "wrong_password")

    assert sign_in_page_ui.check_title("Sign in to GitHub · GitHub")

    sign_in_page_ui.close()
