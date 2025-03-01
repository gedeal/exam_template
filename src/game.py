import time


from .grid import Grid
from .move_commands import show_score, inventory, showlist, print_status
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
jumpvalue=1
total_fruits=8    # Total fruits in the grid
total_fruits_in_basket=0  # total fruits collected in the basket
exit_found = 'noexit'

# TODO - Icons --------------------
trap_a = "\x1b[41mA\x1b[0m"
trap_b = "\x1b[42mB\x1b[0m"
internwall = "\x1b[41m■\x1b[0m"
wall = "\x1b[45m■\x1b[0m"

treasuricon = "\x1b[91mT\x1b[0m"
keyicon = "\x1b[94mK\x1b[0m"
exit_door = "\x1b[42mE\x1b[0m"
victory = "\x1b[92m*\x1b[0m"



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

pickups.exit_game(g)


g.set(50, 2, ' [ Off ]')  # Start with no keys
g.set(50, 5, 0)  # clear Key
g.set(50, 6, 0)  # clear treasure
g.set(50, 8, 0)  # clear points


# TODO: flytta denna till en annan fil ???

def move_point(score, xi, yi, shovel, key, treasure, total_fruits_in_basket,exit_found,jumpvalue):

    maybe_item = g.get(player.pos_x + xi, player.pos_y+yi)

    if shovel==1:
        g.set(50, 2, ' [ On ]' )

    if maybe_item == wall:
        exit_found = wall
        jumpvalue=1
        player.move(0, 0)

    # Cannot move - extern wall
        g.set(37, 10, f" * Can't move - there's an extern wall {wall} **")
        return score, shovel, key, treasure, total_fruits_in_basket, exit_found,jumpvalue


    if maybe_item == internwall:
        if shovel==0:
            player.move(0, 0)
            g.set(37, 10, f" * Can't move - there's an intern wall {internwall} ")

        else:
            player.move(xi, yi)
            print(">> >> >>  Breaking the wall")
            g.set(player.pos_x, player.pos_y, g.empty)
            shovel=0
            g.set(50, 2, ' [ Off ]')


    elif maybe_item == trap_a:
        player.move(xi, yi)
        # I) Fällor - introducera valfri fälla till spelplanen. Om man går på en ruta med en fälla ska man förlora 10 poäng.
        #    Fällan ska ligga kvar så att man kan falla i den flera gånger.
        score = score - 10
        g.set(37, 10, f" * You found a trap, You lost 10 points  **")
        g.set(player.pos_x, player.pos_y, g.empty)
        shovel = 0

        # Create a new trap
        pickups.randomtrap(g)   #- change trap place

    elif maybe_item == keyicon:     # found a key
        player.move(xi, yi)
        g.set(37, 10, f" * You found a key :-)  **")
        key +=1
        g.set(50, 5, key)
        # erase key and save info
        g.set(player.pos_x, player.pos_y, g.empty)

    elif maybe_item == treasuricon:      # Found a treasure
        player.move(xi, yi)

        if key >0 :
            g.set(37, 10, f" * You found a treasure :-)  +100 points  **")
            g.clear(player.pos_x, player.pos_y)
            # erase treasure and save info
            treasure += 1
            g.set(50, 6, treasure)
            score +=100
            key -=1
            if key == 0:
                g.set(37, 10, f" * You have no more keys  :-(  **")
            g.set(50, 5, key)
        else:
            g.set(37, 10, f" * You have no keys for this treasure :-(  **")

    else:
        # G) The floor is lava - för varje steg man går ska man tappa 1 poäng.
        score = score-1
        jumpvalue=1
        player.move(xi, yi)
        if isinstance(maybe_item, pickups.Item):
            # we found something
            score += maybe_item.value
      # Found fruit
            g.set(37, 10, f"* You found a {maybe_item.name}, +{maybe_item.value} points.  ;-) ****")
            #g.set(player.pos_x, player.pos_y, g.empty)
            g.clear(player.pos_x, player.pos_y)
            inventory(fruit_list, maybe_item.name, player.pos_x, player.pos_y,key,treasure)
            # count total fruits found
            total_fruits_in_basket += 1


    g.set(50, 8, score)   # show points

    # M) Exit - slumpa ett "E" på kartan. När man har plockat upp alla ursprungliga saker, kan man gå till exit
    if total_fruits == total_fruits_in_basket:
        exit_found ='exit_prel'
        g.set(37, 10, f"* You can exit now   ;-) ****")

    if maybe_item == exit_door and exit_found == 'exit_prel':
        exit_found='canfinish'


    return score,shovel, key, treasure, total_fruits_in_basket,exit_found,jumpvalue



def move_player (command, score, shovel, key, treasure,total_fruits_in_basket,exit_found,jumpvalue):
    xi = 0
    yi = 0

    # deprecated - changed to show the info in the grid
    # if command=='u':
    #     show_score(score,key)

    if command=="i":
        showlist(fruit_list)

    if command=="a" or command=="d":

        if command=="a":
            xi= -jumpvalue
        else:
            xi= jumpvalue
        temp=move_point(score,xi,yi,shovel,key,treasure,total_fruits_in_basket,exit_found,jumpvalue)
        score=temp[0]
        shovel=temp[1]
        key=temp[2]
        treasure=temp[3]
        total_fruits_in_basket = temp[4]
        exit_found=temp[5]
        jumpvalue=temp[6]


    if command=="w" or command=="s":

        if command=="w":
            yi= -jumpvalue
        else:
            yi= jumpvalue
        temp=move_point(score,xi,yi,shovel,key,treasure,total_fruits_in_basket,exit_found,jumpvalue)
        score = temp[0]
        shovel = temp[1]
        key = temp[2]
        treasure = temp[3]
        total_fruits_in_basket=temp[4]
        exit_found=temp[5]
        jumpvalue=temp[6]

    if command=="k":
        shovel = 1
    # Set shovel
        g.set(50, 2, ' [ On ]' )

    # N) Jump - om man skriver ett "J" innan något av "WASD", ska spelaren hoppa över en ruta.
    #    Man förflyttar sig alltså två steg, men kan förstås bara plocka upp eller interagera med saker där man landar.
    #    Hoppar man in i en vägg blir samman effekt som om man hade gått ett steg på vanligt sätt.
    if command=="j":
        jumpvalue=2
        print('Ready to Jump :', jumpvalue)
    else:
        jumpvalue=1


    return score,shovel, key, treasure, total_fruits_in_basket,exit_found,jumpvalue


# -------------------------------------------------------------STARTING-----------------
command = ""
# Loopa tills användaren trycker Q eller X.
print("\n꧁∙·▫ₒₒ▫ᵒᴼᵒ▫ₒₒ▫꧁      Fruit basket for the brave      ꧂▫ₒₒ▫ᵒᴼᵒ▫ₒₒ▫·∙꧂\n")
# print("\t=>  Use 'i' to show your fruit basket")
# print("\t=>  Use 'u' to show your points ")

while not command.casefold() in ["q", "x"]:
    print_status(g)
    command = input("                                   >> ")
    command = command.casefold()[:1]

    resp=move_player(command, score,shovel,key,treasure, total_fruits_in_basket,exit_found,jumpvalue)
    score =resp[0]
    shovel =resp[1]
    key =resp[2]
    treasure =resp[3]
    total_fruits_in_basket = resp[4]
    exit_found = resp[5]
    jumpvalue=resp[6]

    # print ('total_fruits: ',total_fruits)
    # print ('total_Basket:',total_fruits_in_basket)
    # print('exit_found', exit_found)
    g.set(52, 3, f" = {total_fruits_in_basket}")

    steps +=1
    if steps == 25 and exit_found != 'exit_prel':
        pickups.new_fruit(g)
        steps = 0
        total_fruits += 1

    if exit_found == 'canfinish':
        break

# Hit kommer vi när while-loopen slutar
print(f"\t꧁∙·▫ₒₒ▫꧁  Congratulations - you found the exit door   ꧂▫ₒₒ▫·∙꧂")
print('\n\tTotal score: ', score)
showlist(fruit_list)
time.sleep(1)
print(f"\t꧁∙·▫ₒₒ▫꧁             Thank you for playing!           ꧂▫ₒₒ▫·∙꧂\n")
