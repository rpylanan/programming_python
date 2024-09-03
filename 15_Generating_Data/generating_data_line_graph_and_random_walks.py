#####################################################
# Plotting a simple line graph

# import matplotlib.pyplot as plt
#
# squares = [1, 4, 9, 16, 25]
# fig, ax = plt.subplots()
# ax.plot(squares)
#
# plt.show()

#   Changing the label type and line thickness

import matplotlib.pyplot as plt

# squares = [1, 4, 9, 16, 25]
#
# fig, ax = plt.subplots()
# ax.plot(squares, linewidth=3)
#
# #   Set chart title and label axes
# ax.set_title("Square Numbers", fontsize=24)
# ax.set_xlabel("Value", fontsize=14)
# ax.set_ylabel("Square of Value", fontsize=14)
#
# #   Set size of tick labels
# ax.tick_params(axis='both', labelsize=14)
#
# plt.show()

#    Correcting the Plot

# import matplotlib.pyplot as plt
#
# input_values = [1, 2, 3, 4, 5]
# squares = [1, 4, 9, 16, 25]
#
# plt.style.use('seaborn-v0_8')
# fig, ax = plt.subplots()
# ax.plot(input_values, squares, linewidth=3)
#
# ax.set_title("Square Numbers", fontsize=24)
# ax.set_xlabel("Value", fontsize=14)
# ax.set_ylabel("Square of Value", fontsize=14)
#
# ax.tick_params(axis='both', labelsize=14)
#
# plt.show()

#   Plotting and Styling  Individual Point with scatter()
#
# import matplotlib.pyplot as plt
#
# plt.style.use('seaborn-v0_8')
# fig, ax = plt.subplots()
# ax.scatter(2, 4)
#
# plt.show()

#   Plotting a series of points with scatter()
#
# import matplotlib.pyplot as plt
#
# x_values = [1, 2, 3, 4, 5]
# y_values = [1, 4, 9, 16, 25]
#
# plt.style.use('seaborn-v0_8')
# fig, ax = plt.subplots()
# ax.scatter(x_values, y_values, s=50)
#
# ax.set_title("Square Numbers", fontsize=24)
# ax.set_xlabel("Value", fontsize=14)
# ax.set_ylabel("Square of Value", fontsize=14)
#
# ax.tick_params(axis='both', labelsize=14)
#
# plt.show()

#   Calculating Data Automatically

# import matplotlib.pyplot as plt
#
# x_values = range(1, 1001)
# y_values = [x**2 for x in x_values]
#
# plt.style.use('seaborn-v0_8')
# fig, ax = plt.subplots()
# ax.scatter(x_values, y_values, c='red', s=10)
#
# ax.set_title("Square of Numbers", fontsize=24)
# ax.set_xlabel("Value", fontsize=14)
# ax.set_ylabel("Square of Value", fontsize=14)
#
# ax.tick_params(axis='both', labelsize=14)
#
# ax.axis([0,1100, 0, 1100000])
#
# plt.show()

#   Defining Custom Colors
#   Saving your Plots Automatically
#
# import matplotlib.pyplot as plt
#
# x_values = range(1, 1001)
# y_values = [x**2 for x in x_values]
#
# plt.style.use('seaborn-v0_8')
# fig, ax = plt.subplots()
# ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)
#
# ax.set_title("Square of Numbers", fontsize=24)
# ax.set_xlabel("Value", fontsize=14)
# ax.set_ylabel("Square of Value", fontsize=14)
#
# ax.tick_params(axis='both', labelsize=14)
#
# ax.axis([0, 1100, 0, 1100000])
#
# plt.savefig('squares_plot.png', bbox_inches='tight')

# RANDOM WALKS
#   Creating the RandomWalk() Class
#
# from random import choice
#
# class RandomWalk:
#     """A class to generate random walks."""
#
#     def __init__(self, num_points=5000):
#         """Initialize attributes of a walk."""
#         self.num_points = num_points
#
#         # All walks start at (0, 0)
#         self.x_values = [0]
#         self.y_values = [0]
#
# #   Choosing directions
#     def fill_walk(self):
#         """Calculate all the points in the walk"""
#
#         # Keep taking steps until the walk reaches the desired length.
#         while len(self.x_values) < self.num_points:
#
#             # Decide which direction to go and how far to go in that direction.
#             x_direction = choice([1, -1])
#             x_distance = choice([0, 1, 2, 3, 4])
#             x_step = x_direction * x_distance
#
#             y_direction = choice([1, -1])
#             y_distance = choice([0, 1, 2, 3, 4])
#             y_step = y_direction * y_distance
#
#             # Reject moves that go nowhere
#             if x_step == 0 and y_step == 0:
#                 continue
#
#             # calculate the new position
#             x = self.x_values[-1] + x_step
#             y = self.y_values[-1] + y_step
#
#             self.x_values.append(x)
#             self.y_values.append(y)

#   Plotting the Random Walk
#
# import matplotlib.pyplot as plt
#
# from random_walk import RandomWalk
#
# # make a random walk
# rw = RandomWalk()
# rw.fill_walk()
#
# # Plot the points in the walk.
# plt.style.use('classic')
# fig, ax = plt.subplots()
# ax.scatter(rw.x_values, rw.y_values, s=15)
# plt.show()

#   Generating multiple random walks

# import matplotlib.pyplot as plt
#
# from random_walk import RandomWalk
#
# # Keep making new walks as long as the program is active
#
# while True:
#     # Make a random walk
#     rw = RandomWalk()
#     rw.fill_walk()
#
#     plt.style.use('classic')
#     fig, ax = plt.subplots()
#     ax.scatter(rw.x_values, rw.y_values, s=15)
#     plt.show()
#
#     keep_running = input("Make another walk? (y/n): ")
#     if keep_running == 'n':
#         break

#   Styling the walk
#       Coloring the points

# import matplotlib.pyplot as plt
#
# from random_walk import RandomWalk
#
# while True:
#     rw = RandomWalk()
#     rw.fill_walk()
#
#     plt.style.use('classic')
#     fig, ax = plt.subplots()
#     point_numbers = range(rw.num_points)
#     ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=15)
#     plt.show()
#
#     keep_running = input("Make another walk? (y/n): ")
#     if keep_running == 'n':
#         break

#       Plotting the starting and ending points

# import matplotlib.pyplot as plt
#
# from random_walk import RandomWalk
#
# while True:
#     rw = RandomWalk()
#     rw.fill_walk()
#
#     plt.style.use('classic')
#     fig, ax = plt.subplots()
#     point_numbers = range(rw.num_points)
#     ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=15)
#
#     # Emphasize the first and last points
#     ax.scatter(0, 0, c='green', edgecolors='none', s=100)
#     ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)
#
#     plt.show()
#
#     keep_runnig = input("Make another walk? (y/n): ")
#     if keep_running == 'n':
#         break

#       Cleaning up the axes

# import matplotlib.pyplot as plt
#
# from random_walk import RandomWalk
#
# while True:
#     rw = RandomWalk()
#     rw.fill_walk()
#
#     plt.style.use('classic')
#     # dimension of the plotting window in inches
#     fig, ax = plt.subplots(figsize=(15, 9))
#     point_numbers = range(rw.num_points)
#     ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=15)
#     ax.scatter(0, 0 , c='green', edgecolors='none', s=100)
#     ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)
#
#     # Remove the axes
#     ax.get_xaxis().set_visible(False)
#     ax.get_yaxis().set_visible(False)
#
#     plt.show()
#
#     keep_running = input("Make another walk? (y/n): ")
#     if keep_running == 'n':
#         break







