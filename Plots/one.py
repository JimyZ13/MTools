import matplotlib.pyplot as plt
import numpy as np
data_string = """

"""

matrix_data = np.loadtxt(data_string.splitlines())

x = matrix_data[:, 0]
y = matrix_data[:, 1]

fig, ax = plt.subplots()

ax.plot(x, y, 'bo-', label='')

ax.set_title('Convergence of total energy of vc-relaxation of InP')

ax.grid(True)

ax.legend()

plt.show()