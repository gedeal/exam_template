# Run only this tests
# pytest test/test_pickups.py -srA


from src.grid import Grid
from src.pickups import *


def test_pickups__randomize():
    expected = None
    g = Grid()
    resp = randomize(g)

    # print('Response_1: ',resp)
    assert expected == resp


def test_pickups__new_fruit():
    expected = None

    g = Grid()
    resp = new_fruit(g)

    # print('Response_1: ',resp)
    assert expected == resp


def test_pickups__exit_game():
    expected = None

    g = Grid()
    resp = exit_game(g)

    # print('Response_1: ',resp)
    assert expected == resp


def test_pickups__randomtrap():
    expected = None

    g = Grid()
    resp = randomtrap(g)

    # print('Response_1: ',resp)
    assert expected == resp


def test_pickups__randomkey():
    expected = None

    g = Grid()
    resp = randomkey(g)

    # print('Response_1: ',resp)
    assert expected == resp

def test_pickups__randomtreasure():
    expected = None

    g = Grid()
    resp = randomtreasure(g)

    # print('Response_1: ',resp)
    assert expected == resp

