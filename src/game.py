import time
from code import InteractiveConsole
from linecache import clearcache
from operator import length_hint
from traceback import print_tb

from .grid import Grid
from .move_commands import show_score, inventory, showlist, print_status
from .pickups import Item
from .player import Player
from . import pickups

import os
os.system("cls" if os.name == "nt" else "clear")

player = Player(int(Grid.width/2), int(Grid.height/2) )   #  x= 1-36 , y= 1-12
score = 0
fruit_list = []
shovel = 0
key = 0
treasure = 0
steps = 0

# TODO - Icons --------------------
trap_a = "\x1b[41mA\x1b[0m"
trap_b = "\x1b[42mB\x1b[0m"
internwall = "\x1b[41m■\x1b[0m"
wall = "\x1b[45m■\x1b[0m"

treasuricon = "\x1b[91mT\x1b[0m"
keyicon = "\x1b[94mK\x1b[0m"


# ------------------------

g = Grid()
g.set_player(player)
g.make_walls()
g.intern_walls()
pickups.randomize(g)

# time.sleep(1)
pickups.randomtrap(g)

pickups.randomkey(g)
pickups.randomtreasure(g)

g.set(50, 3, ' [ Off ]')  # Start with no keys
g.set(50, 6, 0)  # clear Key
g.set(50, 7, 0)  # clear points



# TODO: flytta denna till en annan fil ???

def move_point(score, xi, yi, shovel, key,treasure):
    maybe_item = g.get(player.pos_x + xi, player.pos_y+yi)

    if shovel==1:
        g.set(50, 3, ' [ On ]' )

    if maybe_item == internwall:
        if shovel==0:
            g.set(37, 9, f" * Can't move - there's an intern wall {internwall} ")
            player.move(0,0)
        else:
            print(">> >> >>  Breaking the wall")
            player.move(xi, yi)
            g.set(player.pos_x, player.pos_y, g.empty)
            shovel=0
            g.set(50, 3, ' [ Off ]')

    elif maybe_item == wall:
    # Can no move - extern wall
        g.set(37, 9, f" * Can't move - there's an extern wall {wall} **")
        player.move(0, 0)

    elif maybe_item == trap_a:
        # I) Fällor - introducera valfri fälla till spelplanen. Om man går på en ruta med en fälla ska man förlora 10 poäng.
        #    Fällan ska ligga kvar så att man kan falla i den flera gånger.
        score = score - 10
        g.set(37, 9, f" * You found a trap, You lost 10 points  **")
        player.move(xi, yi)
        g.set(player.pos_x, player.pos_y, g.empty)
        shovel = 0

        # Create a new trap
        pickups.randomtrap(g)   #- change trap place


    elif maybe_item == keyicon:     # found a key
        g.set(37, 9, f" * You found a key :-)  **")
        player.move(xi, yi)
        key +=1
        g.set(50, 6, key)
        # erase key and save info
        g.set(player.pos_x, player.pos_y, g.empty)

    elif maybe_item == treasuricon:      # Found a treasure
        player.move(xi, yi)

        if key >0 :
            g.set(37, 9, f" * You found a treasure :-)  +100 points  **")
            g.clear(player.pos_x, player.pos_y)
            # erase treasure  and save info
            treasure += 1
            score +=100
            key -=1
            if key == 0:
                g.set(37, 9, f" * You have no more keys  :-(  **")
            g.set(50, 6, key)
        else:
            g.set(37, 9, f" * You have no keys for this treasure :-(  **")

    else:
        # print("OK", maybe_item)
        player.move(xi, yi)
        # G) The floor is lava - för varje steg man går ska man tappa 1 poäng.
        score = score-1
        if isinstance(maybe_item, pickups.Item):
            # we found something
            score += maybe_item.value
      # Found fruit
            g.set(37, 9, f"* You found a {maybe_item.name}, +{maybe_item.value} points.  ;-) ****")
            #g.set(player.pos_x, player.pos_y, g.empty)
            g.clear(player.pos_x, player.pos_y)
            inventory(fruit_list, maybe_item.name, player.pos_x, player.pos_y,key,treasure)


    g.set(50, 7, score)   # show points
    return score,shovel, key, treasure

def move_player (command, score, shovel, key, treasure ):
    xi = 0
    yi = 0
    g.set(37, 9, f"")


    if command=="u":
        show_score(score,key)

    if command=="i":
        showlist(fruit_list)

    if command=="a" or command=="d":
        if command=="a":
            xi= -1
        else:
            xi= 1
        temp=move_point(score,xi,yi,shovel,key,treasure)
        score=temp[0]
        shovel=temp[1]
        key=temp[2]
        treasure=temp[3]

    if command=="w" or command=="s":
        if command=="w":
            yi= -1
        else:
            yi= 1
        temp=move_point(score,xi,yi,shovel,key,treasure)
        score = temp[0]
        shovel = temp[1]
        key = temp[2]
        treasure = temp[3]

    if command=="k":
        shovel = 1
    # Set shovel
        g.set(50, 3, ' [ On ]' )
    return score, shovel, key, treasure


# -------------------------------------------------------------STARTING-----------------
command = ""
# Loopa tills användaren trycker Q eller X.
print("\n꧁∙·▫ₒₒ▫ᵒᴼᵒ▫ₒₒ▫꧁      Fruit basket for the brave      ꧂▫ₒₒ▫ᵒᴼᵒ▫ₒₒ▫·∙꧂\n")
# print("\t=>  Use 'i' to show your fruit basket")
# print("\t=>  Use 'u' to show your points ")

while not command.casefold() in ["q", "x"]:
    print_status(g)

    # command = input("** Use WASD to move, Q/X to quit. ")
    command = input("----------------------------------->> ")
    command = command.casefold()[:1]

    # print("Location X:", player.pos_x , "  Location Y :", player.pos_y )
    resp=move_player(command, score,shovel,key,treasure)
    score =resp[0]
    shovel =resp[1]
    key =resp[2]
    treasure =resp[3]

    steps +=1
    if steps == 25:
        pickups.new_fruit(g)
        steps = 0


# Hit kommer vi när while-loopen slutar
print("\n꧁∙·▫ₒₒ▫꧁   Thank you for playing!  ꧂▫ₒₒ▫·∙꧂\n")
