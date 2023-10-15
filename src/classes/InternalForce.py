class InternalForce():
    def __init__(self, slap, p_d, a_x_bracket, a_y_bracket, a_x_opennes, a_y_opennes):
        self.slap = slap,
        self.a_x_bracket = a_x_bracket,
        self.a_y_bracket = a_y_bracket,
        self.a_x_opennes = a_x_opennes,
        self.a_xy_opennes = a_y_opennes,
        self.p_d = p_d,
        self.internal_forces = self.get_internal_forces()

    def get_internal_forces(self):
        return {
            "x_bracket": self.calculate_internal_forces(self, self.a_x_bracket, self.p_d, self.l_s),
            "x_opennes": self.calculate_internal_forces(self, self.a_x_opennes, self.p_d, self.l_s),
            "y_bracket": self.calculate_internal_forces(self, self.a_y_bracket, self.p_d, self.l_s),
            "y_opennes": self.calculate_internal_forces(self, self.a_y_opennes, self.p_d, self.l_s),
        }

    def calculate_internal_forces(self, a, p_d, l_s):
        return a * p_d * l_s**2
