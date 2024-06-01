import pytest


@pytest.fixture
def struct():
    return 6


def test_import(struct):
    assert struct == 6
