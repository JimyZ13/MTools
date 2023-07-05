import matplotlib.pyplot as plt
import numpy as np

text_form = '''

'''


matrices = []
current_matrix = []
for line in text_form.strip().split('\n'):
    if line.strip():  # Skip empty lines
        current_matrix.append([float(num) for num in line.strip().split()])
    elif current_matrix:
        matrices.append(current_matrix)
        current_matrix = []

if current_matrix:
    matrices.append(current_matrix)

# Plot each matrix as a separate line
for matrix in matrices:
    matrix = np.array(matrix)
    plt.plot(matrix[:, 0], matrix[:, 1])

# Vertical Line plots
vertical_lines = [0.0] 
for x in vertical_lines:
    plt.axvline(x, color='red', linestyle='--')


plt.title('Silicon Band Structure')
plt.show()