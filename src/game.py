from linecache import clearcache

from .grid import Grid
from .player import Player
from . import pickups

import os
# os.system('cls' if os.name == 'nt' else 'clear')

player = Player(17, 5)   #  x= 1-34 , y= 1-10
score = 0
inventory = []

g = Grid()
g.set_player(player)
g.make_walls()
pickups.randomize(g)


# TODO: flytta denna till en annan fil
def print_status(game_grid):
    """Visa spelvärlden och antal poäng."""
    # print("\n--------------------------------------")
    print(f"\tYour total:  {score} points.")
    print(game_grid)


def move_player (command,score):
    xi = 0
    yi = 0

    if command=='a' or command=='d':
        if command=='a':
            xi= -1
        else:
            xi= 1

    if command=='w' or command=='s':
        print('This is the command : ',command)
        if command=='w':
            yi= -1
        else:
            yi= 1
    # print ('X:',xi ,'Y:',yi)

    maybe_item = g.get(player.pos_x + xi, player.pos_y+yi)
    player.move(xi, yi)

    if isinstance(maybe_item, pickups.Item):
        # we found something
        score += maybe_item.value
        print('\n********************************************')
        print(f"\tYou found a {maybe_item.name}, +{maybe_item.value} points.")
        print('********************************************')
        #g.set(player.pos_x, player.pos_y, g.empty)
        g.clear(player.pos_x, player.pos_y)

    return score



command = "a"
# Loopa tills användaren trycker Q eller X.
while not command.casefold() in ["q", "x"]:
    print_status(g)

    command = input("Use WASD to move, Q/X to quit. ")
    command = command.casefold()[:1]

    print('Location X:', player.pos_x )
    print('Location Y :', player.pos_y )

    # if (1 < player.pos_x <34) and (1 < player.pos_y <10) :
    #     print('OK')
    score = move_player(command, score)
        # print(score)




    # if command == "d" and player.can_move(1, 0, g):  # move right
    #     # TODO: skapa funktioner, så vi inte behöver upprepa så mycket kod för riktningarna "W,A,S"
    #     maybe_item = g.get(player.pos_x + 1, player.pos_y)
    #     player.move(1, 0)
    #
    #
    #     if isinstance(maybe_item, pickups.Item):
    #         # we found something
    #         score += maybe_item.value
    #         print(f"You found a {maybe_item.name}, +{maybe_item.value} points.")
    #         #g.set(player.pos_x, player.pos_y, g.empty)
    #         g.clear(player.pos_x, player.pos_y)
    #
    # if command == "a" and player.can_move(-1, 0, g):  # move left
    #     maybe_item = g.get(player.pos_x-1 , player.pos_y)
    #     player.move(-1, 0)
    #
    #     if isinstance(maybe_item, pickups.Item):
    #         # we found something
    #         score += maybe_item.value
    #         print(f"You found a {maybe_item.name}, +{maybe_item.value} points.")
    #         #g.set(player.pos_x, player.pos_y, g.empty)
    #         g.clear(player.pos_x, player.pos_y)
    #
    # if command == "w" and player.can_move(0, -1, g):  # move left
    #     maybe_item = g.get(player.pos_x , player.pos_y-1)
    #     player.move(0, -1)
    #
    #     if isinstance(maybe_item, pickups.Item):
    #         # we found something
    #         score += maybe_item.value
    #         print(f"You found a {maybe_item.name}, +{maybe_item.value} points.")
    #         #g.set(player.pos_x, player.pos_y, g.empty)
    #         g.clear(player.pos_x, player.pos_y)
    #
    # if command == "s" and player.can_move(0, 1, g):  # move left
    #     maybe_item = g.get(player.pos_x , player.pos_y+1)
    #     player.move(0, 1)
    #
    #     if isinstance(maybe_item, pickups.Item):
    #         # we found something
    #         score += maybe_item.value
    #         print(f"You found a {maybe_item.name}, +{maybe_item.value} points.")
    #         #g.set(player.pos_x, player.pos_y, g.empty)
    #         g.clear(player.pos_x, player.pos_y)



# Hit kommer vi när while-loopen slutar
print("Thank you for playing!")
