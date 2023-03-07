import pytest


@pytest.mark.check
def test_check_name(newUser):
    """Username check test."""
    assert newUser.name == "Yurii"


@pytest.mark.check
def test_check_second_name(newUser):
    """Test for checking the user's second name."""
    assert newUser.second_name == "Mudryk"
