import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

n = int(input("Introduce la cantidad de cargas: "))

cargas = []
for i in range(n):
    x = float(input("Introduce la posición en x de la carga {}: ".format(i+1)))
    y = float(input("Introduce la posición en y de la carga {}: ".format(i+1)))
    z = float(input("Introduce la posición en z de la carga {}: ".format(i+1)))
    carga = (x,y,z)
    cargas.append(carga)

k = 9e9 # Constante de Coulomb
fuerzas = np.zeros((n,n)) # Crear una matriz de ceros para almacenar las fuerzas
for i in range(n):
    for j in range(i+1,n):
        dx = cargas[i][0] - cargas[j][0]
        dy = cargas[i][1] - cargas[j][1]
        dz = cargas[i][2] - cargas[j][2]
        r = np.sqrt(dx**2 + dy**2 + dz**2)
        fuerza = k * cargas[i][3] * cargas[j][3] / r**2
        fuerzas[i,j] = fuerza
        fuerzas[j,i] = -fuerza # La fuerza es atractiva o repulsiva dependiendo del signo de las cargas

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
for carga in cargas:
    ax.scatter(carga[0], carga[1], carga[2], s=100, c='r', marker='o')
plt.show()

for i in range(n):
    for j in range(i+1,n):
        dx = cargas[i][0] - cargas[j][0]
        dy = cargas[i][1] - cargas[j][1]
        dz = cargas[i][2] - cargas[j][2]
        r = np.sqrt(dx**2 + dy**2 + dz**2)
