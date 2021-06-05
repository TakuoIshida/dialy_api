from utils.func import *

import pytest


def test_add_01():
    assert add(2.5, 3.5) == 6.0


def test_add_02():
    assert add(-2.5, -3.5) == -6.0


def test_add_03():
    assert add(0, 3.5) == 3.5

# 複数のテストを同時に走らせる場合


@pytest.mark.parametrize(
    "x,y,expect", [
        (2, 3, 5),
        (1, 2, 3),
        (4, 5, 9)
    ]
)
def test_add_multi(x, y, expect: int):
    assert x + y == expect
