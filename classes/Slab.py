class Slab():
    def __init__(self, dimension, edges_type, floor_name, floor_type, moment_coefficients, config):
        self.x = dimension[0]
        self.y = dimension[1]
        self.floor_name = floor_name
        self.floor_type = floor_type
        self.edges_type = edges_type
        self.perimeter = sum(dimension) * 2
        self.continuous_edge = self.__continues_edge_total()
        self.edge_proportion = self.x/self.y if self.x > self.y else self.y/self.x
        self.how_floor_work = 'single direction' if self.edge_proportion > 2 else 'double direction'
        self.a_s = self.__continues_edge_proportion()
        self.config = config
        self.ls_n = self.__determine_ls_n()
        self.slab_thicknes = self.__determining_slab_thickness()
        self.moment_coefficients = moment_coefficients

    def __str__(self):
        return f"Floor: {self.floor_name}\n" \
            f"Dimensions: {self.x} x {self.y}\n" \
            f"Edge Proportion: {self.edge_proportion}\n" \
            f"How Floor Works: {self.how_floor_work}"

    def __determining_slab_thickness(self):
        # h >0 80m TS(500)
        if (self.floor_type == 'normal'):
            return (self.ls_n / (15 + 20 / self.edge_proportion)) * (1-(self.a_s/4))
        return self.ls_n / 12

    def __continues_edge_proportion(self):
        return self.continuous_edge / self.perimeter

    def __continues_edge_total(self):
        return self.edges_type[0] * self.x + self.edges_type[1] * self.y + self.edges_type[2] * self.x + self.edges_type[3] * self.y

    def __determine_ls_n(self):
        x = self.x
        y = self.y
        beam_front_dimension = self.config['beam_front_dimension'] * 10
        if (self.floor_type == 'balcony'):
            return y * 1000 - beam_front_dimension / 2 if x > y else x * 1000 - beam_front_dimension / 2

        return y * 1000 - beam_front_dimension if x > y else x * 1000 - beam_front_dimension

    def write_to_file(self, filename):
        with open(filename, 'a') as file:
            file.write(f"Floor: {self.floor_name}\n")
            file.write(f"Type: {self.floor_type}\n")
            file.write(f"a_s: {self.a_s}\n")
            file.write(f"Dimensions: {self.x} x {self.y}\n")
            file.write(f"Edge Proportion: {self.edge_proportion}\n")
            file.write(f"How Floor Works: {self.how_floor_work}\n")
            file.write(f"ls: {self.ls_n}\n")
            file.write(f"Slab Thickness: {self.slab_thicknes}\n")
            file.write(f"-----------------------------------\n")
