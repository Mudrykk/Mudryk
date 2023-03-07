import pytest


@pytest.mark.change
def test_remove_name(newUser):
    """Test to verify user deletion."""
    newUser.name = ""
    assert newUser.name == ""


@pytest.mark.check
def test_name(newUser):
    """Username check test."""
    assert newUser.name == "Yurii"


@pytest.mark.check
def test_second_name(newUser):
    """Test for checking the user's second name."""
    assert newUser.second_name == "Mudryk"
