
from classes.Slab import *


class InternalForce():
    def __init__(self, slab: Slab, p_d):
        self.slab = slab
        self.a_x_bracket = slab.moment_coefficients["a_x_bracket"]
        self.a_y_bracket = slab.moment_coefficients["a_y_bracket"]
        self.a_x_opennes = slab.moment_coefficients["a_x_opennes"]
        self.a_y_opennes = slab.moment_coefficients["a_y_opennes"]
        self.p_d = p_d
        self.internal_forces = self.get_internal_forces()

    def get_internal_forces(self):
        return {
            "x_bracket": self.calculate_internal_forces(self.a_x_bracket, self.p_d, self.slab.ls_n),
            "x_opennes": self.calculate_internal_forces(self.a_x_opennes, self.p_d, self.slab.ls_n),
            "y_bracket": self.calculate_internal_forces(self.a_y_bracket, self.p_d, self.slab.ls_n),
            "y_opennes": self.calculate_internal_forces(self.a_y_opennes, self.p_d, self.slab.ls_n),
        }

    def calculate_internal_forces(self, a, p_d, l_s):
        return a * p_d * l_s**2
