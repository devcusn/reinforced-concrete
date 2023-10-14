class Slab():
    def __init__(self, dimension, type, floor_name):
        self.x = dimension[0]
        self.y = dimension[1]
        self.type = type
        self.name = floor_name
        self.edge_proportion = self.x/self.y if self.x > self.y else self.y/self.x
        self.how_floor_work = 'single direction' if self.edge_proportion > 2 else 'double direction'

    def __str__(self):
        return f"Floor: {self.name}\n" \
            f"Dimensions: {self.x} x {self.y}\n" \
            f"Edge Proportion: {self.edge_proportion}\n" \
            f"How Floor Works: {self.how_floor_work}"

    def determining_slab_thickness():
        return 'calculate here'
