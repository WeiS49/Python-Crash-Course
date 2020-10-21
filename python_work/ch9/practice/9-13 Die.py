
from random import randint

class Die():
    """
    Simulated six-sided dice
    """
    def __init__(self, sides = 6):
        """ Initialize the property of dice. """
        self.sides = sides

    def roll_die(self):
        """ Roll the dice. """
        return randint(1, self.sides)

Die6 = Die()

for i in range(10):
    print(Die6.roll_die())

print()

Die10 = Die(10)
for i in range(10):
    print(Die10.roll_die())

print()

Die20 = Die(20)
for i in range(10):
    print(Die20.roll_die())









