import numpy as np

def add_vector_to_matrix(matrix_str, vector):
    # Convert the matrix string to a numpy array
    rows = matrix_str.strip().split('\n')
    matrix = np.array([list(map(float, row.split())) for row in rows])
    
    # Check if the dimensions match
    if matrix.shape[1] != len(vector):
        raise ValueError("Vector dimensions do not match the matrix columns.")
    
    # Add the vector to each row of the matrix
    result = matrix + vector
    
    return result

matrix_str = '''

'''
vector = [0, 0, 20]

result = add_vector_to_matrix(matrix_str, vector)
output_file = "add.txt"

with open(output_file, 'w') as file:
    for row in result:
        file.write(' '.join(str(element) for element in row))
        file.write('\n')
