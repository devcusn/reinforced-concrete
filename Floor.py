class Floor():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.edge_proportion = x/y if x > y else y/x
        self.how_floor_work = 'single direction' if self.edge_proportion > 2 else 'double direction'
