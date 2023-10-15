from classes.Slab import *
from classes.Load import *
from helper.helper import *

l_y_1 = 4.2
l_y_2 = 6.0
l_x_1 = 4.6
l_x_2 = 4.6
l_x_3 = 5.8
a = 1.2
h = 3

concrete_type = 'C30'
soil_type = 'ZD'
q_t = 420
beam_front_dimension = 30  # cm
# deprem verisi
[latitude, longitude] = [38.65, 39.65]

print("""
                    |-b2-|
         |----|-----|----|----|----|
         | d1 | d2  | d3 |d2  | d1 |  
         |    |     |    |    |    |
      ----------------------------------
      |b1| d4 | d5  |    | d6 | d4 |b1 |
      |  |    |     |    |    |    |   |
      ----------------------------------
         |d1  |d2   |d3  |d2  |d1  |
         |    |     |    |    |    |
         |----|-----|----|----|----|
                    |-b2-|
      """)

slabs_data = {
    'd2': {"dimension": [l_x_1, l_y_1], "edges_type": [0, 1, 1, 0], "slab_type": "normal"},
    'd2': {"dimension": [l_x_2, l_y_1], "edges_type": [0, 1, 1, 1], "slab_type": "normal"},
    'd3': {"dimension": [l_x_3, l_y_1], "edges_type": [1, 1, 1, 1], "slab_type": "normal"},
    'd4': {"dimension": [l_x_1, l_y_2], "edges_type": [1, 1, 1, 1], "slab_type": "normal"},
    'd5': {"dimension": [l_x_2, l_y_2], "edges_type": [1, 0, 1, 1], "slab_type": "normal"},
    'd6': {"dimension": [l_x_2, l_y_2], "edges_type": [1, 1, 1, 1], "slab_type": "normal"},
    'b1': {"dimension": [l_x_3, a], "edges_type": [0, 0, 0, 1], "slab_type": "balcony"},
    'b2': {"dimension": [a, l_y_2], "edges_type": [1, 0, 0, 0], "slab_type": "balcony"}
}


slabs = [Slab(value['dimension'], value["edges_type"], key, value["slab_type"], {"beam_front_dimension": beam_front_dimension})
         for key, value in slabs_data.items()]


[s.write_to_file('slabs') for s in slabs]
# determination of loads
# TS498 -live load values page 12 table 7
# for housing = 2 KN/m^2
# for balcony = 5 KN/m^2 <= 10m^2

loads_data_for_normal_slabs = {
    "marble": {"m": 0.03, "per_load": 27},
    "reinforced_concrete": {"m": 0.12, "per_load": 25},
    "plaster": {"m": 0.02, "per_load": 20},
    "screed_mortar": {"m": 0.05, "per_load": 21},
}

loads_data_for_balcony_slabs = {
    "ceramic": {"m": 0.07, "per_load": 26},
    "reinforced_concrete": {"m": 0.12, "per_load": 25},
    "plaster": {"m": 0.02, "per_load": 20},
    "screed_mortar": {"m": 0.05, "per_load": 21}
}


loads_for_normal_slabs = [Load(key, value["m"], value["per_load"])
                          for key, value in loads_data_for_normal_slabs.items()]

dead_load_for_normal = sum([l.total_load for l in loads_for_normal_slabs])

pd_normal = get_total_load(
    2, dead_load_for_normal)

loads_for_balcony_slabs = [Load(key, value["m"], value["per_load"])
                           for key, value in loads_data_for_balcony_slabs.items()]

dead_load_for_balcony = sum([l.total_load for l in loads_for_balcony_slabs])

pd_balcony = get_total_load(
    5, dead_load_for_balcony)


# calculation of internal forces
