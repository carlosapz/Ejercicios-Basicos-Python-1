import math
import matplotlib.pyplot as plt

class Carga:
    def __init__(self, x, y, z, q):
        self.x = x
        self.y = y
        self.z = z
        self.q = q

def main():
    cargas = []
    print("Bienvenido al programa para calcular la fuerza electrostática entre cargas")
    sistema = input("¿En qué sistema de unidades desea ingresar las cargas? (C/G): ")

    n = int(input("Ingrese el número de cargas que desea agregar: "))
    for i in range(n):
        print("Carga #", i+1)
        x = float(input("Ingrese la posición en x de la carga: "))
        y = float(input("Ingrese la posición en y de la carga: "))
        z = float(input("Ingrese la posición en z de la carga: "))
        q = float(input("Ingrese el valor de la carga: "))
        cargas.append(Carga(x, y, z, q))

    print("Cargas ingresadas:")
    for i in range(n):
        print("Carga #", i+1, " - x:", cargas[i].x, "y:", cargas[i].y, "z:", cargas[i].z, "q:", cargas[i].q)

    print("Seleccione dos cargas para calcular la fuerza electrostática entre ellas")
    carga1 = int(input("Carga 1: "))
    carga2 = int(input("Carga 2: "))

    distancia = math.sqrt((cargas[carga2-1].x - cargas[carga1-1].x)**2 + (cargas[carga2-1].y - cargas[carga1-1].y)**2 + (cargas[carga2-1].z - cargas[carga1-1].z)**2)

    fuerza = (9 * (10**9) * cargas[carga1-1].q * cargas[carga2-1].q) / (distancia**2)

    print("La distancia entre las cargas es:", distancia, "unidades")
    print("La fuerza electrostática entre las cargas es:", fuerza, "N")

    # Crear gráfico
    x_vals = [carga.x for carga in cargas]
    y_vals = [carga.y for carga in cargas]
    z_vals = [carga.z for carga in cargas]

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x_vals, y_vals, z_vals, s=100)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    # Conectar las dos cargas con una línea
    ax.plot([cargas[carga1-1].x, cargas[carga2-1].x], [cargas[carga1-1].y, cargas[carga2-1].y], [cargas[carga1-1].z, cargas[carga2-1].z], c='r')
    plt.show()

if __name__ == '__main__':
    main()
