import pygal
from random import randint


class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll(self):
        return randint(1, self.sides)


die = Die()
die2 = Die(10)


results = []
for roll in range(50000):
    result = die.roll() + die2.roll()
    results.append(result)


frequencies = []
max_result = die.sides + die2.sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)


hist = pygal.Bar()
hist.title = 'results of rolling D6 + D10 50000 times'
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16']
hist.x_title = 'result'
hist.y_title = 'frequency of result'

hist.add('D6 + D10', frequencies)
hist.render_to_file('D10_D6.svg')
