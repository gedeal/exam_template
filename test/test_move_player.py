# Run only this tests
# pytest test/test_move_player.py -srA

from src.game import *

def test_move_player_test1__game():
    expected = 0
    resp = move_player('q', 0,0,0,0,0)
    score =resp[0]
    shovel =resp[1]
    key =resp[2]
    treasure =resp[3]
    total_fruits_in_basket = resp[4]
    print('Response_1: ',resp)
    assert expected == score



def test_move_player_test2__game():
    expected = 1
    resp = move_player('q', 1,1,1,1,1)
    score = resp[0]
    shovel = resp[1]
    key = resp[2]
    treasure = resp[3]
    total_fruits_in_basket = resp[4]
    print('Response_2: ', resp)
    assert expected == score

def test_move_player_test3__game():
    expected = -1
    resp = move_player('a', 0,0,0,0,0)
    score =resp[0]
    shovel =resp[1]
    key =resp[2]
    treasure =resp[3]
    total_fruits_in_basket = resp[4]
    print('Response_3: ',resp)
    assert expected == score

def test_move_player_test4__game():
    expected = 1
    resp = move_player('k', 0,0,0,0,0)
    score =resp[0]
    shovel =resp[1]
    key =resp[2]
    treasure =resp[3]
    total_fruits_in_basket = resp[4]
    print('Response_4: ',resp)
    assert expected == shovel
