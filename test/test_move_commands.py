# Run only this tests
# pytest test/test_move_commands.py -srA
from src.game import fruit_list
from src.move_commands import *


def test_move_command__show_score_0():
    expected = 0
    score=5
    key=0
    resp=show_score(5,0)
    print('Response_1: ',resp)
    assert expected == resp

def test_move_command__show_score_2():
    expected = 1
    score=5
    key=2
    resp=show_score(5,2)
    print('Response_1: ',resp)
    assert expected == resp


def test_move_command__inventory():
    expected= ['test',1,2]
    fruit=['test',1,2]
    newfruit='baba'
    posx=12
    posy=10
    resp=inventory(['test',1,2],newfruit,posx,posy,1,2)
    resp_a=resp[0]
    resp_b=resp[1]
    resp_c=resp[2]

    assert newfruit == resp_a
    assert posx == resp_b
    assert posy == resp_c


