import pytest

# The function we want to test
def get_user_status(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age < 18:
        return "minor"
    return "adult"

# 1. Test a standard success case
def test_user_status_minor():
    assert get_user_status(10) == "minor"

# 2. Test an "edge case" (exactly 18)
def test_user_status_edge_case():
    assert get_user_status(18) == "adult"

# 3. Test that the function correctly raises an error
def test_user_status_invalid_age():
    with pytest.raises(ValueError, match="Age cannot be negative"):
        get_user_status(-5)
