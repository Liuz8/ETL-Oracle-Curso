import numpy as np
precio_inmuebles = np.array([10000, 120000, 11000, 200000])
#precio_inmuebles_lima = precio_inmuebles
precio_inmuebles_lima = np.copy(precio_inmuebles)
precio_inmuebles[0] = 120000
print(precio_inmuebles)
print(precio_inmuebles_lima)