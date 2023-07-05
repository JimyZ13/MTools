import numpy as np

def parse_matrix(matrix_str):
    lines = matrix_str.strip().split('\n')
    matrix = []
    for line in lines:
        row = [float(val) for val in line.strip().split()]
        matrix.append(row)
    return np.array(matrix)

def get_bounded_points(matrix_str, x_range, y_range, z_range):
    matrix = parse_matrix(matrix_str)
    bounded_points = []
    for point in matrix:
        x, y, z = point
        if x_range[0] <= x <= x_range[1] and y_range[0] <= y <= y_range[1] and z_range[0] <= z <= z_range[1]:
            bounded_points.append(point)
    return bounded_points

n = 5
matrix_str = """

"""
x_range = (6, 17.6) 
y_range = (0, 5.86)  
z_range = (5, 24) 

bounded_points = get_bounded_points(matrix_str, x_range, y_range, z_range)
i = 0
for coord in bounded_points:
    i += 1
    print(f"     {coord[0]:.9f}         {coord[1]:.9f}         {coord[2]:.9f}")

print(i)
