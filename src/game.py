from linecache import clearcache
from operator import length_hint
from traceback import print_tb

from .grid import Grid
from .move_commands import show_score, inventory, showlist, print_status
from .pickups import Item
from .player import Player
from . import pickups

import os
os.system('cls' if os.name == 'nt' else 'clear')


# print("WIDTH",Grid.width)
# print("Height",Grid.height)


player = Player(int(Grid.width/2), int(Grid.height/2) )   #  x= 1-36 , y= 1-12
score = 0
fruit_list = []

g = Grid()
g.set_player(player)
g.make_walls()
g.intern_walls()

pickups.randomize(g)


# TODO: flytta denna till en annan fil

def move_point(score, xi, yi):
    maybe_item = g.get(player.pos_x + xi, player.pos_y+yi)
    # newscore = score
    internwall = "\x1b[41m■\x1b[0m"
    wall  = "\x1b[45m■\x1b[0m"

    if maybe_item == internwall:
        print("**  Can't move - there's an internwall",internwall)
        player.move(0,0)
    elif maybe_item == wall:
        print("**  Can't move - there's an external wall", wall)
        player.move(0, 0)
    else:
        # print('OK', maybe_item)
        player.move(xi, yi)
        # G) The floor is lava - för varje steg man går ska man tappa 1 poäng.
        score = score-1
        if isinstance(maybe_item, pickups.Item):
            # we found something
            score += maybe_item.value
            print('\n********************************************')
            print(f"   You found a {maybe_item.name}, +{maybe_item.value} points.")
            print('********************************************')
            #g.set(player.pos_x, player.pos_y, g.empty)
            g.clear(player.pos_x, player.pos_y)
            inventory(fruit_list, maybe_item.name, player.pos_x, player.pos_y)

    return score

def move_player (command,score):
    xi = 0
    yi = 0

    if command=='u':
        show_score(score)

    if command=='i':
        showlist(fruit_list)

    if command=='a' or command=='d':
        if command=='a':
            xi= -1
        else:
            xi= 1
        score=move_point(score,xi,yi)

    if command=='w' or command=='s':
        if command=='w':
            yi= -1
        else:
            yi= 1
        score=move_point(score, xi, yi)

    return score

# -------------------------------------------------------------STARTING-----------------
command = ""
# Loopa tills användaren trycker Q eller X.
print("\n꧁∙·▫ₒₒ▫꧁   Fruit basket for the brave  ꧂▫ₒₒ▫·∙꧂\n")
print("\t=>  Use 'i' to show your fruit basket")
print("\t=>  Use 'u' to show your points ")

while not command.casefold() in ["q", "x"]:
    print_status(g)

    command = input("Use WASD to move, Q/X to quit. ")
    command = command.casefold()[:1]

    # print('Location X:', player.pos_x , '  Location Y :', player.pos_y )
    score=move_player(command, score)
    # print ('\t\t\tScore:',score)

# Hit kommer vi när while-loopen slutar

print("\n꧁∙·▫ₒₒ▫꧁   Thank you for playing!  ꧂▫ₒₒ▫·∙꧂\n")
