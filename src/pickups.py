
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

def randomtrap(grid):
    # Put a Trap
    a= "\x1b[43mA\x1b[0m"
    b= "\x1b[42mB\x1b[0m"
    while True:
        # slumpa en position tills vi hittar en som är ledig
        x = grid.get_random_x()
        y = grid.get_random_y()
        if grid.is_empty(x, y):
            grid.set(x, y, a)
            break  # avbryt while-loopen, fortsätt med nästa varv i for-loopen

    # while True:
    #     # slumpa en position tills vi hittar en som är ledig
    #     x = grid.get_random_x()
    #     y = grid.get_random_y()
    #     if grid.is_empty(x, y):
    #         grid.set(x, y, b)
    #         break  # avbryt while-loopen, fortsätt med nästa varv i for-loopen

    return None


#K) Nycklar och kistor - slumpa minst en nyckel och lika många kistor på spelplanen.
def randomkey(grid):
    # Put a Key
    k = "\x1b[94mK\x1b[0m"
    for i in range(2):
        print(i)
        while True:
            # slumpa en position tills vi hittar en som är ledig
            x = grid.get_random_x()
            y = grid.get_random_y()
            if grid.is_empty(x, y):
                grid.set(x, y, k)
                break  # avbryt while-loopen, fortsätt med nästa varv i for-loopen
    return None

def randomthreasure(grid):
    # Put a threasure
    # k = "\x1b[43mT\x1b[0m"
    t="\x1b[91mT\x1b[0m"
    for i in range(2):
        print(i)
        while True:
            # slumpa en position tills vi hittar en som är ledig
            x = grid.get_random_x()
            y = grid.get_random_y()
            if grid.is_empty(x, y):
                grid.set(x, y, t)
                break  # avbryt while-loopen, fortsätt med nästa varv i for-loopen
    return None