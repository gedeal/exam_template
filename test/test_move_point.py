# Run only this tests
# pytest test/test_move_player.py -srA

from src.game import *


def test_move_point_test1__game():
    expected = 124

    resp = move_point(125, 0,0,0,0,0,0)
    score =resp[0]
    shovel =resp[1]
    key =resp[2]
    treasure =resp[3]
    total_fruits_in_basket = resp[4]


    print('Response_1: ',resp)
    assert expected == score
