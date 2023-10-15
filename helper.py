def get_total_load(q, g):
    return 1.6*q + 1.4*g


def calculate_internal_forces(a, p_d, l_s):
    return a * p_d * l_s**2
