from Dice import Dice
import matplotlib.pyplot as plt

die1 = Dice()
die2 = Dice()

results = []
for each_event in range(1000):
    result = die1.roll_die() + die2.roll_die()
    results.append(result)

frequencies = []
max_result = die1.num_sides + die2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

x_values = list(range(2, max_result+1))
y_values = frequencies

plt.bar(x_values, y_values)
plt.title('Trying out with histogram', fontsize=15)
plt.xlabel('The x-axis')
plt.ylabel('The y-axis')

plt.show()