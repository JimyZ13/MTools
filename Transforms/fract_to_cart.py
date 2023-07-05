import numpy as np

def string_to_array(matrix_str):
    # Split the string into rows
    rows = matrix_str.strip().split('\n')

    # Split each row into individual elements
    elements = [row.split() for row in rows]

    # Convert elements to floats
    float_elements = [[float(elem) for elem in row] for row in elements]

    # Convert the list of lists to a NumPy array
    array = np.array(float_elements)

    return array

matrix_str = """


"""

matrix_array = string_to_array(matrix_str)

a1 = np.array([23.476000 ,0.000000, -40.661624])
a2 = np.array([0.000000 ,23.476000 ,0.000000])
a3 = np.array([81.323249, 0.000000 ,46.952000])

A = np.vstack([a1, a2, a3]).T
A_inv = np.linalg.inv(A)

Y = matrix_array

# Compute the cartesian coordinates
X = np.matmul(A, Y.T).T

# Perform the inverse operation to get fractional coordinates
Y_ = np.matmul(A_inv, X.T).T

# X is cartesian, Y is fractional, Y_ is fractional checker

for coord in X:
    print(f"     {coord[0]:.9f}         {coord[1]:.9f}         {coord[2]:.9f}")

file_path = 'cart.txt'
np.savetxt(file_path, X, fmt='%.9f', delimiter='     ', newline='\n')