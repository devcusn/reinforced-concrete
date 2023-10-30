class BracketBalance():
    def __init__(self, bracket_1, bracket_2):
        self.bracktet_1 = bracket_1
        self.brackter_2 = bracket_2
        [self.great_force, self.small_force] = [bracket_1.force,
                                                bracket_2.force] if bracket_1.force > bracket_2.force else [bracket_2.force, bracket_1.force]
        self.proportion = self.great_force / self.small_force
        self.balancedResult = self.getResult()

    def getResult(self):
        M1 = self.calc_modified_force(self.bracktet_1)
        M2 = self.calc_modified_force(self.bracktet_2)
        return {"M1": M1, "M2": M2}

    def calc_modified_force(self, bracket):
        delta_m = 2/3 * (self.great_force - self.small_force)
        if (bracket.force == self.great_force):
            other_bracket_length = self.bracket_2.length if bracket.length == self.bracket_1.length else bracket.length
            return bracket.force - delta_m * (other_bracket_length / (self.bracket_1.length + self.bracket_2.length))
        return bracket.force + delta_m * (other_bracket_length / (self.bracket_1.length + self.bracket_2.length))
