import numpy as np
from scipy.spatial.transform import Rotation

def complementary_filter_update(initial_rotation, angular_velocity, linear_acceleration, dt):
    g = np.array([1, 0, 0])
    rotation_current = Rotation.from_rotvec(angular_velocity * dt)
    rotation_matrix = initial_rotation * rotation_current
    g_prime = rotation_matrix.apply(linear_acceleration)
    g_prime = g_prime / np.linalg.norm(g_prime)

    omega_acc = np.cross(g_prime, g)
    omega_acc_norm = np.linalg.norm(omega_acc)
    if omega_acc_norm != 0:
        omega_acc = omega_acc / omega_acc_norm

    angle = np.arccos(np.dot(g_prime, g))
    q_acc = Rotation.from_rotvec(angle * omega_acc).as_quat()

    e_m = abs(np.linalg.norm(linear_acceleration) / 9.81 - 1)
    if e_m >= 0.2:
        alpha = 0
    elif e_m <= 0.1:
        alpha = 1
    else:
        alpha = -10 * (e_m - 0.1) + 1

    q_acc_prime = ((1 - alpha) * np.array([0, 0, 0, 1])) + (alpha * q_acc)
    correct_rotation = Rotation.from_quat(q_acc_prime) * rotation_matrix

    return correct_rotation
