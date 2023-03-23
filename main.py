import pytest


def always_returns_true():
    print("Hello Ms. Lovelace")
    return True

def test_always_returns_true():
    assert always_returns_true()
