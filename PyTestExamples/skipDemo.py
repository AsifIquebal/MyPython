import pytest


@pytest.mark.skip(reason="no way of currently testing this")
def test_the_unknown():
    assert True


import sys
@pytest.mark.skipif(sys.version_info < (3, 9), reason="requires python3.9")
def test_the_unknown_conditionally():
    assert True


def test_the_known():
    assert True
