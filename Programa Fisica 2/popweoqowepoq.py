import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def calcular_fuerza(q1, q2, r):
    k = 9e9  # Constante de Coulomb
    return k * q1 * q2 / (r ** 2)

def distancia(p1, p2):
    return math.sqrt(sum([(a - b) ** 2 for a, b in zip(p1, p2)]))

def pedir_cargas(n):
    cargas = []
    for i in range(n):
        q = float(input(f"Introduzca la carga {i + 1}: "))
        x = float(input(f"Introduzca la coordenada x de la carga {i + 1}: "))
        y = float(input(f"Introduzca la coordenada y de la carga {i + 1}: "))
        z = float(input(f"Introduzca la coordenada z de la carga {i + 1}: "))
        cargas.append((q, x, y, z))
    return cargas

def mostrar_cargas(cargas):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    xs = [c[1] for c in cargas]
    ys = [c[2] for c in cargas]
    zs = [c[3] for c in cargas]
    ax.scatter(xs, ys, zs)
    plt.show()

def main():
    sistemas = ["SI", "CGS"]
    sistema = input(f"Introduzca el sistema de unidades ({'/'.join(sistemas)}): ")
    if sistema not in sistemas:
        print(f"Sistema de unidades no válido. Los sistemas disponibles son: {', '.join(sistemas)}")
        return

    n = int(input("Introduzca el número de cargas: "))
    cargas = pedir_cargas(n)
    mostrar_cargas(cargas)

    for i in range(n):
        for j in range(i + 1, n):
            q1, x1, y1, z1 = cargas[i]
            q2, x2, y2, z2 = cargas[j]
            r = distancia((x1, y1, z1), (x2, y2, z2))
            if sistema == "SI":
                print(f"Fuerza entre la carga {i + 1} y la carga {j + 1}: {calcular_fuerza(q1, q2, r)} N")
                print(f"Distancia entre la carga {i + 1} y la carga {j + 1}: {r} m")
            elif sistema == "CGS":
                print(f"Fuerza entre la carga {i + 1} y la carga {j + 1}: {calcular_fuerza(q1, q2, r) * 1e5} dyn")
                print(f"Distancia entre la carga {i + 1} y la carga {j + 1}: {r * 1e2} cm")

if __name__ == "__main__":
    main()
