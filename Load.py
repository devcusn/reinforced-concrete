class Load:
    def __init__(self, name, m, per_load):
        self.name = name
        self.m_2 = m
        self.per_load = per_load
        self.total_load = m * per_load
