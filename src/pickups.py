# from src.game import treasuricon, keyicon, trap_a, trap_b
import random

trap_a = "\x1b[41mA\x1b[0m"
trap_b = "\x1b[42mB\x1b[0m"
internwall = "\x1b[41m■\x1b[0m"
wall = "\x1b[45m■\x1b[0m"

treasuricon = "\x1b[91mT\x1b[0m"
keyicon = "\x1b[94mK\x1b[0m"
exit_door = "\x1b[42mE\x1b[0m"

class Item:
    """Representerar saker man kan plocka upp."""

# D) Fruktsallad - alla frukter ska vara värda 20 poäng i stället för 10.
#     def __init__(self, name, value=10, symbol="#"):     # Change value
#     def __init__(self, name, value=20, symbol="\x1b[92m#\x1b[0m"):     # Change value
    def __init__(self, name, value=20, symbol="#"):     # Change value
        self.name = name
        self.value = value
        self.symbol = symbol

    def __str__(self):
        return self.symbol


pickups = [Item("carrot"), Item("apple"), Item("strawberry"), Item("cherry"), Item("watermelon"), Item("radish"), Item("cucumber"), Item("meatball")]


def randomize(grid):
    for item in pickups:
        while True:
            # slumpa en position tills vi hittar en som är ledig
            x = grid.get_random_x()
            y = grid.get_random_y()
            if grid.is_empty(x, y):
                grid.set(x, y, item)
                break  # avbryt while-loopen, fortsätt med nästa varv i for-loopen
    return None


def new_fruit(grid):
    while True:
        random_fruit = random.choice(pickups)
        # slumpa en position tills vi hittar en som är ledig
        x = grid.get_random_x()
        y = grid.get_random_y()
        if grid.is_empty(x, y):
            grid.set(x, y, random_fruit)
            break  # avbryt while-loopen, fortsätt med nästa varv i for-loopen
    return None


def exit_game(grid):
    while True:
        x = grid.get_random_x()
        y = grid.get_random_y()
        if grid.is_empty(x, y):
            grid.set(x, y, exit_door)
            break  # avbryt while-loopen, fortsätt med nästa varv i for-loopen
    return None


def randomtrap(grid):
    # Put a Trap

    while True:
        # slumpa en position tills vi hittar en som är ledig
        x = grid.get_random_x()
        y = grid.get_random_y()
        if grid.is_empty(x, y):
            grid.set(x, y, trap_a)
            break  # avbryt while-loopen, fortsätt med nästa varv i for-loopen

    return None


#K) Nycklar och kistor - slumpa minst en nyckel och lika många kistor på spelplanen.
def randomkey(grid):
    # Put a Key

    for i in range(2):
        while True:
            # slumpa en position tills vi hittar en som är ledig
            x = grid.get_random_x()
            y = grid.get_random_y()
            if grid.is_empty(x, y):
                grid.set(x, y, keyicon)
                break  # avbryt while-loopen, fortsätt med nästa varv i for-loopen
    return None

def randomtreasure(grid):
    # Put a treasure
    for i in range(2):
        while True:
            # slumpa en position tills vi hittar en som är ledig
            x = grid.get_random_x()
            y = grid.get_random_y()
            if grid.is_empty(x, y):
                grid.set(x, y, treasuricon)
                break  # avbryt while-loopen, fortsätt med nästa varv i for-loopen
    return None