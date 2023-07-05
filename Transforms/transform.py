import numpy as np
from math import radians

def rotate_coordinates(coord_string, axis, angle):
    # Split the coordinate string into individual coordinates
    coordinates = coord_string.strip().split('\n')
    
    # Parse each coordinate and store as a numpy array
    parsed_coords = []
    for coord in coordinates:
        parsed_coords.append(np.array([float(c) for c in coord.split()]))

    # Normalize the rotation axis vector
    axis = np.array(axis)
    axis = axis / np.linalg.norm(axis)

    # Convert the angle to radians
    angle_rad = radians(angle)

    # Compute the components of the rotation matrix
    cos_theta = np.cos(angle_rad)
    sin_theta = np.sin(angle_rad)
    one_minus_cos_theta = 1 - cos_theta

    # Construct the rotation matrix
    rotation_matrix = np.array([
        [
            cos_theta + axis[0]**2 * one_minus_cos_theta,
            axis[0] * axis[1] * one_minus_cos_theta - axis[2] * sin_theta,
            axis[0] * axis[2] * one_minus_cos_theta + axis[1] * sin_theta
        ],
        [
            axis[1] * axis[0] * one_minus_cos_theta + axis[2] * sin_theta,
            cos_theta + axis[1]**2 * one_minus_cos_theta,
            axis[1] * axis[2] * one_minus_cos_theta - axis[0] * sin_theta
        ],
        [
            axis[2] * axis[0] * one_minus_cos_theta - axis[1] * sin_theta,
            axis[2] * axis[1] * one_minus_cos_theta + axis[0] * sin_theta,
            cos_theta + axis[2]**2 * one_minus_cos_theta
        ]
    ])

    # Perform the rotation on each coordinate
    rotated_coords = []
    for coord in parsed_coords:
        rotated_coords.append(np.dot(rotation_matrix, coord))

    # Convert the rotated coordinates to Cartesian form
    cartesian_coords = []
    for coord in rotated_coords:
        cartesian_coords.append(f"{coord[0]:.6f} {coord[1]:.6f} {coord[2]:.6f}")

    # Return the rotated coordinates as a formatted string
    return '\n'.join(cartesian_coords)

coordinates = """
"""

rotated_coordinates = rotate_coordinates(coordinates, [0, 23.4759998322, 0], 60)
print(rotated_coordinates)