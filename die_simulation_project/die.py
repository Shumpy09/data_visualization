from random import randint

class Die():
    """Klasa przedstawiająca pojedynczą kość do gry"""


    def __init__(self, num_sides=6):
        """Przyjęcie założenia, że kośc do gry ma postać sześcianu"""

        self.num_sides = num_sides

    def roll(self):
        """Zwrot wartości z zakresi od 1 do liczby ścianek, które ma kość do gry"""

        return randint(1, self.num_sides)