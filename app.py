from classes.Slab import *
from classes.Load import *
from classes.InternalForce import *
from helper.helper import *
from config import *

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
    'd1': {"dimension": [l_x_1, l_y_1], "edges_type": [0, 1, 1, 0], "slab_type": "normal", "moment_coefficients": {
        "a_x_bracktet": 0.049,
        "a_x_opennes": 0.037,
        "a_y_bracktet": 0.056,
        "a_y_opennes": 0.042

    }},
    'd2': {"dimension": [l_x_2, l_y_1], "edges_type": [0, 1, 1, 1], "slab_type": "normal", "moment_coefficients": {
        "a_x_bracktet": 0.042,
        "a_x_opennes": 0.031,
        "a_y_bracktet": 0.047,
        "a_y_opennes": 0.035

    }},
    'd3': {"dimension": [l_x_3, l_y_1], "edges_type": [1, 1, 1, 1], "slab_type": "normal", "moment_coefficients": {
        "a_x_bracktet": 0.033,
        "a_x_opennes": 0.025,
        "a_y_bracktet": 0.054,
        "a_y_opennes": 0.041

    }},
    'd4': {"dimension": [l_x_1, l_y_2], "edges_type": [1, 1, 1, 1], "slab_type": "normal", "moment_coefficients": {
        "a_x_bracktet": 0.033,
        "a_x_opennes": 0.025,
        "a_y_bracktet": 0.033,
        "a_y_opennes": 0.025

    }},
    'd5': {"dimension": [l_x_2, l_y_2], "edges_type": [1, 0, 1, 1], "slab_type": "normal", "moment_coefficients": {
        "a_x_bracktet": 0.042,
        "a_x_opennes": 0.031,
        "a_y_bracktet": 0.057,
        "a_y_opennes": 0.042

    }},
    'd6': {"dimension": [l_x_2, l_y_2], "edges_type": [1, 1, 1, 1], "slab_type": "normal", "moment_coefficients": {
        "a_x_bracktet": 0.033,
        "a_x_opennes": 0.025,
        "a_y_bracktet": 0.033,
        "a_y_opennes": 0.025

    }},
    'b1': {"dimension": [l_x_3, a], "edges_type": [0, 0, 0, 1], "slab_type": "balcony", "moment_coefficients": {
        "a_x_bracktet": 0.052,
        "a_x_opennes": 0.052,
        "a_y_bracktet": 0.052,
        "a_y_opennes": 0.052

    }},
    'b2': {"dimension": [a, l_y_2], "edges_type": [1, 0, 0, 0], "slab_type": "balcony", "moment_coefficients": {
        "a_x_bracktet": 0.052,
        "a_x_opennes": 0.052,
        "a_y_bracktet": 0.052,
        "a_y_opennes": 0.052

    }}
}


slabs = [Slab(value['dimension'], value["edges_type"], key, value["slab_type"], value["moment_coefficients"], {"beam_front_dimension": beam_front_dimension})
         for key, value in slabs_data.items()]


[s.write_to_file('slabs') for s in slabs]
# determination of loads
# TS498 -live load values page 12 table 7
# for housing = 2 KN/m^2
# for balcony = 5 KN/m^2 <= 10m^2

loads_data_for_normal_slabs = {
    "marble": {"m": 0.03, "per_load": 27},
    "reinforced_concrete": {"m": reinforced_concrete_slab_thickness, "per_load": 25},
    "plaster": {"m": 0.02, "per_load": 20},
    "screed_mortar": {"m": 0.05, "per_load": 21},
}

loads_data_for_balcony_slabs = {
    "ceramic": {"m": 0.07, "per_load": 26},
    "reinforced_concrete": {"m": reinforced_concrete_slab_thickness, "per_load": 25},
    "plaster": {"m": 0.02, "per_load": 20},
    "screed_mortar": {"m": 0.05, "per_load": 21}
}


loads_for_normal_slabs = [Load(key, value["m"], value["per_load"])
                          for key, value in loads_data_for_normal_slabs.items()]

dead_load_for_normal = sum([l.total_load for l in loads_for_normal_slabs])

pd_normal = get_total_load(
    2, dead_load_for_normal)
print(pd_normal)
loads_for_balcony_slabs = [Load(key, value["m"], value["per_load"])
                           for key, value in loads_data_for_balcony_slabs.items()]

dead_load_for_balcony = sum([l.total_load for l in loads_for_balcony_slabs])

pd_balcony = get_total_load(
    5, dead_load_for_balcony)


# calculation of internal forces

internal_forces = [InternalForce(slab, pd_normal) for slab in slabs]

[i.write_to_file('internal_forces') for i in internal_forces]
