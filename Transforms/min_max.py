import numpy as np

def parse_matrix(matrix_str):
    lines = matrix_str.strip().split('\n')
    matrix = []
    for line in lines:
        row = [float(val) for val in line.strip().split()]
        matrix.append(row)
    return np.array(matrix)

def find_min_max(matrix_str):
    matrix = parse_matrix(matrix_str)
    min_x = np.min(matrix[:, 0])
    max_x = np.max(matrix[:, 0])
    min_y = np.min(matrix[:, 1])
    max_y = np.max(matrix[:, 1])
    min_z = np.min(matrix[:, 2])
    max_z = np.max(matrix[:, 2])
    return min_x, max_x, min_y, max_y, min_z, max_z

matrix_str = """

"""

min_x, max_x, min_y, max_y, min_z, max_z = find_min_max(matrix_str)
print("X range:", min_x, "-", max_x)
print("Y range:", min_y, "-", max_y)
print("Z range:", min_z, "-", max_z)