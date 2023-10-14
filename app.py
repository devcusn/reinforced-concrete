from Floor import *

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

floors = {'d1': [l_x_1, l_y_1],
          'd2': [l_x_2, l_y_1],
          'd3': [l_x_3, l_y_1],
          'd4': [l_x_1, l_y_2],
          'd5': [l_x_2, l_y_2],
          'd6': [l_x_2, l_y_2],
          'b1': [l_x_3, a],
          'b1': [a, l_y_2]}