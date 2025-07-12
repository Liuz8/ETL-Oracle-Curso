import numpy as np

clientes = np.array([[1, 'Juan', 30, 'Calle A', 100, 'electrónicos'],
                     [2, 'Maria', 25, 'Calle B', 200, 'moda'],
                     [3, 'Pedro', 35, 'Calle C', 50, 'deportes']])

intencion_compras = clientes[:,4:]
# Segunda respuesta correcta        intencion_compras = clientes[:,4:]

print(intencion_compras)