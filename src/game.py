from linecache import clearcache
from operator import length_hint
from traceback import print_tb

from .grid import Grid
from .player import Player
from . import pickups


import os
os.system('cls' if os.name == 'nt' else 'clear')

player = Player(17, 5)   #  x= 1-34 , y= 1-10
score = 0
fruit_list = []

g = Grid()
g.set_player(player)
g.make_walls()
g.intern_walls()


pickups.randomize(g)



# TODO: flytta denna till en annan fil

def show_score():           # Show score now
    # print('Your score is : ', score)
    print(f"** Your total score is: \n**      {score} points.")



def inventory(fruit, pos_x,pos_y):
# - E) Inventory - alla saker som man plockar upp ska sparas i en lista.
    fruit =[fruit, pos_x,pos_y]
    fruit_list.append(fruit)



def showlist():
# - F) Nytt kommando: "i", skriver ut innehållet i spelarens inventory.

    mylist=len(fruit_list)
    # print(mylist)
    if mylist==0:
        print("  ** You have not collect fruits yet  :-(")
    else:
        print(f"** Fruit basket ({mylist}) **")
        for lista in fruit_list:
            item = fruit_list.index(lista)+1
            print(f"   [{item}]  {lista[0]} ")


def print_status(game_grid):
    """Visa spelvärlden och antal poäng."""
    # print("\n--------------------------------------")

    print(game_grid)


def move_player (command,score):
    xi = 0
    yi = 0

    if command=='u':
        show_score()

    if command=='i':
        showlist()

    if command=='a' or command=='d':
#G) The floor is lava - för varje steg man går ska man tappa 1 poäng.
        score = score-1
        # print('New score : ', score)
        if command=='a':
            xi= -1
        else:
            xi= 1

    if command=='w' or command=='s':
# G) The floor is lava - för varje steg man går ska man tappa 1 poäng.
        score = score-1
        # print('New score : ', score)
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
        print(f"   You found a {maybe_item.name}, +{maybe_item.value} points.")
        print('********************************************')
        #g.set(player.pos_x, player.pos_y, g.empty)
        g.clear(player.pos_x, player.pos_y)
        inventory(maybe_item.name, player.pos_x, player.pos_y)

    return score



command = ""
# Loopa tills användaren trycker Q eller X.
print("Use 'i' to show the fruit basket")
print("Use 'u' to show the points ")



while not command.casefold() in ["q", "x"]:
    print_status(g)

    command = input("Use WASD to move, Q/X to quit. ")
    command = command.casefold()[:1]

    # print('Location X:', player.pos_x , ' - Location Y :', player.pos_y )

    if (0 < player.pos_x <35) and (0 < player.pos_y <11) :
        # print('OK')
        score = move_player(command, score)
        # print(score)
    else:
        print('NOtOK')
        score = move_player('No', score)





# Hit kommer vi när while-loopen slutar
print("Thank you for playing!")
