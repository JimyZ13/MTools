import matplotlib.pyplot as plt
import numpy as np

data_string1 = """

"""

data_string2 = """

"""

data_string3 = """

"""

data_string4 = """

"""

matrix_data1 = np.loadtxt(data_string1.splitlines())
matrix_data2 = np.loadtxt(data_string2.splitlines())
matrix_data3 = np.loadtxt(data_string3.splitlines())
matrix_data4 = np.loadtxt(data_string4.splitlines())

x = matrix_data1[:, 0]
y = matrix_data1[:, 1]

x2 = matrix_data2[:, 0]
y2 = matrix_data2[:, 1]

x3 = matrix_data3[:, 0]
y3 = matrix_data3[:, 1]

x4 = matrix_data4[:, 0]
y4 = matrix_data4[:, 1]

fig, ax = plt.subplots()

ax.plot(x, y, 'bo--', label='6')
ax.plot(x2, y2, 'ro--', label='8')
ax.plot(x3, y3, 'go--', label='12')
ax.plot(x4, y4, 'yo-', label='16')

ax.set_title('Aluminum Smear Convergence with all k values')

ax.grid(True)

ax.legend()

# Show the plot
plt.show()