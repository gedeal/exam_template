import random


class Grid:
    """Representerar spelplanen. Du kan ändra standardstorleken och tecknen för olika rutor. """
    width = 36
    height = 12
    empty = "."  # Tecken för en tom ruta
    wall  = "\x1b[45m■\x1b[0m"   # Tecken för en ogenomtränglig vägg
# https: // www.fileformat.info / info / emoji / list.htm
    internwall = "\x1b[41m■\x1b[0m"   # Tecken för en intern vägg

    # internwall = "\u2139"   # Tecken för en intern vägg


    def __init__(self):
        """Skapa ett objekt av klassen Grid"""
        # Spelplanen lagras i en lista av listor. Vi använder "list comprehension" för att sätta tecknet för "empty" på varje plats på spelplanen.
        self.data = [[self.empty for y in range(self.width)] for z in range(
            self.height)]


    def get(self, x, y):
        """Hämta det som finns på en viss position"""
        return self.data[y][x]

    def set(self, x, y, value):
        """Ändra vad som finns på en viss position"""
        self.data[y][x] = value

    def set_player(self, player):
        self.player = player

    def clear(self, x, y):
        """Ta bort item från position"""
        self.set(x, y, self.empty)

    def __str__(self):
        """Gör så att vi kan skriva ut spelplanen med print(grid)"""
        xs = ""
        for y in range(len(self.data)):
            row = self.data[y]
            for x in range(len(row)):
                if x == self.player.pos_x and y == self.player.pos_y:
                    xs += "\x1b[104m@\x1b[0m"

                    # xs += "\u26F5"
                else:
                    xs += str(row[x])
            xs += "\n"
        return xs


    def make_walls(self):
        """Skapa väggar runt hela spelplanen"""
        for i in range(self.height):
            self.set(0, i, self.wall)
            self.set(self.width - 1, i, self.wall)

        for j in range(1, self.width - 1):
            self.set(j, 0, self.wall)
            self.set(j, self.height - 1, self.wall)


    # Används i filen pickups.py
    def get_random_x(self):
        """Slumpa en x-position på spelplanen"""
        return random.randint(0, self.width-1)

    def get_random_y(self):
        """Slumpa en y-position på spelplanen"""
        return random.randint(0, self.height-1)


    def is_empty(self, x, y):
        """Returnerar True om det inte finns något på aktuell ruta"""
        return self.get(x, y) == self.empty


    def intern_walls(self):
    # H) Använd for -loopar för att skapa flera, sammanhängande väggar på kartan.

    #Horizontal
        for i in range(4):
            self.set(6, i+3, self.internwall)
            # self.set(self.width - 1, i, self.internwall)

        for i in range(5):
            self.set(27, i+5, self.internwall)
            # self.set(self.width - 1, i, self.internwall)

    #Vertical
        for i in range(6):
            self.set(i+20, 3, self.internwall)
            # self.set(self.width - 1, i, self.internwall)

        for i in range(3):
            self.set(i+ 10, 8, self.internwall)
            # self.set(self.width - 1, i, self.internwall)