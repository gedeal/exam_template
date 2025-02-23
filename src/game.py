import time
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

player = Player(int(Grid.width/2), int(Grid.height/2) )   #  x= 1-36 , y= 1-12
score = 0
fruit_list = []
shovel = 0
key = 0
theasure = 0

g = Grid()
g.set_player(player)
g.make_walls()
g.intern_walls()
pickups.randomize(g)

# time.sleep(1)
pickups.randomtrap(g)

pickups.randomkey(g)
pickups.randomthreasure(g)



# TODO: flytta denna till en annan fil ???

def move_point(score, xi, yi, shovel, key,theasure):
    maybe_item = g.get(player.pos_x + xi, player.pos_y+yi)
    internwall = "\x1b[41m■\x1b[0m"
    wall  = "\x1b[45m■\x1b[0m"
    trap_a= "\x1b[43mA\x1b[0m"
    trap_b= "\x1b[42mB\x1b[0m"

    if shovel==1:
        print ('** Shovel at hand ;-)')

    if maybe_item == internwall:
        if shovel==0:
            print(internwall ," Can't move - there's an intern wall")
            player.move(0,0)
        else:
            print('>> >> >>  Breaking the wall')
            player.move(xi, yi)
            g.set(player.pos_x, player.pos_y, g.empty)
            shovel=0
            print("** Shovel removed :-( ")

    elif maybe_item == wall:
        print(wall," Can't move - there's an external wall")
        player.move(0, 0)

    elif maybe_item == trap_a:
        # I) Fällor - introducera valfri fälla till spelplanen. Om man går på en ruta med en fälla ska man förlora 10 poäng.
        #    Fällan ska ligga kvar så att man kan falla i den flera gånger.
        player.move(xi, yi)
        score = score - 10
        print('\n********************************************')
        print(f"   You found a trap, You lost 10 points ")
        print('********************************************')
    # elif maybe_item == trap_b:
    #     print('Trap B')

    elif maybe_item == "\x1b[94mK\x1b[0m":     # found a key
        print('You found a key')
        player.move(xi, yi)
        key +=1

        #TODO -- erase key and save info


    elif maybe_item == "\x1b[91mT\x1b[0m":      # Found a theasure
        print('You found a theasure')
        player.move(xi, yi)
        theasure +=1

        #TODO -- erase theasure  and save info

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
            inventory(fruit_list, maybe_item.name, player.pos_x, player.pos_y,key,theasure)

    return score,shovel, key, theasure

def move_player (command, score, shovel, key, theasure ):
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
        temp=move_point(score,xi,yi,shovel,key,theasure)
        score=temp[0]
        shovel=temp[1]
        key=temp[2]
        theasure=temp[3]

    if command=='w' or command=='s':
        if command=='w':
            yi= -1
        else:
            yi= 1
        temp=move_point(score,xi,yi,shovel,key,theasure)
        score = temp[0]
        shovel = temp[1]
        key = temp[2]
        theasure = temp[3]

    if command=='k':
        shovel = 1
        print('** Shovel at hand ;-)')

    return score,shovel,key,theasure

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
    resp=move_player(command, score,shovel,key,theasure)
    score =resp[0]
    shovel =resp[1]
    key =resp[2]
    theasure =resp[3]

    # print ('\t\t\tScore:',score)
    # print ('\t\t\tshovel:',shovel)

# Hit kommer vi när while-loopen slutar
# print("\t _/\\_  Thank you for playing! _/\\_  \n")
print("\n꧁∙·▫ₒₒ▫꧁   Thank you for playing!  ꧂▫ₒₒ▫·∙꧂\n")
