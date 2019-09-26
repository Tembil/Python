"""
import matplotlib.pyplot as plt
"""
import math

new_x = []
new_y = []
tempValue = 0.0
step = round(1.0/500,4)

for i in range(500):
	new_x.append(round(tempValue,4))
	tempValue += step

for x in new_x:
	tempY = math.sin(4 * math.pi * x) * math.exp(-5 * x)
	new_y.append(tempY)

print(new_x, new_y)
# fig, ax = plt.subplots()

# ax.fill(new_x, new_y, zorder=10) 
# ax.grid(True, zorder=5)
# plt.show()