"""
Project matplotlib
Function Grid()
Version 3.4 -> 3.7
"""

import matplotlib.pyplot as plt
# Implementation of matplotlib function
from mpl_toolkits.axes_grid1.axes_grid import Grid

fig, ax = plt.subplots()
Grid(fig, (1, 2, 1), (1, 1), label_mode='sfsdsdf')

plt.show()
