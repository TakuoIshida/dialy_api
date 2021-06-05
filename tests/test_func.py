from utils.func import *


def test_add_01():
    assert add(2.5, 3.5) == 6.0


def test_add_02():
    assert add(-2.5, -3.5) == -6.0


def test_add_03():
    assert add(0, 3.5) == 3.5
