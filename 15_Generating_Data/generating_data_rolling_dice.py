
# ROLLING DICE WITH PLOTLY

#   Creating the Die Class

# from random import randint
#
# class Die:
#     """A class representing a single die."""
#
#     def __init__(self, num_sides=6):
#         """Assume a six-sided die."""
#         self.num_sides = num_sides
#
#     def roll(self):
#         """Return a random value between 1 and number of sides"""
#         return randint(1, self.num_sides)

#   Rolling the Die

# from die import Die
#
# # Create a D6
# die = Die()
#
# # Make some rolls, and store results in a list.
# results = []
# for roll_num in range(100):
#     result = die.roll()
#     results.append(result)
#
# print(results)

#   Analyzing the Results.

# from die import Die
#
# die = Die()
#
# results = []
# for roll_num in range(1000):
#     result = die.roll()
#     results.append(result)
#
# frequencies = []
# for value in range(1, die.num_sides+1):
#     frequency = results.count(value)
#     frequencies.append(frequency)
#
# print(frequencies)

#   Making a histogram
#
# from plotly.graph_objs import Bar, Layout
# from plotly import offline
# from die import Die
#
# die = Die()
#
# results = []
# for roll_num in range(1000):
#     result = die.roll()
#     results.append(result)
#
# frequencies = []
# for value in range(1, die.num_sides+1):
#     frequency = results.count(value)
#     frequencies.append(frequency)
#
# # Visualize the results
# x_values = list(range(1, die.num_sides+1))
# data = [Bar(x=x_values, y=frequencies)]
#
# x_axis_config = {'title': 'Result'}
# y_axis_config = {'title': 'Frequency of Result'}
# my_layout = Layout(title='Results of rolling one D6 1000 times', xaxis=x_axis_config, yaxis=y_axis_config)
# offline.plot({'data': data, 'layout': my_layout}, filename='d6.html')

#   Rolling two dice

from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# Create two D6 dice.
die_1 = Die()
die_2 = Die()

# Make some rolls, and store results in a list
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Analyze the results.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results.
x_values = list(range(2, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling two D6 dice 1000 times', xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6_d6.html')










