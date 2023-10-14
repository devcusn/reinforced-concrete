from Slab import *

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


floors = [Slab(value['dimension'], value["edges_type"], key, value["slab_type"], {"beam_front_dimension": beam_front_dimension})
          for key, value in slabs_data.items()]

print(floors[0].slab_thicknes)
