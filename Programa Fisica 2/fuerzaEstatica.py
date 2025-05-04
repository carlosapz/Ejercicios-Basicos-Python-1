import math
import matplotlib.pyplot as plt

# Definir la constante de Coulomb en unidades SI
k = 8.987 * 10**9 

# Función para calcular la fuerza electrostática entre dos cargas q1 y q2 en una distancia r
def calc_fuerza_electrostatica(q1, q2, r):
    return k * q1 * q2 / r**2

# Función para calcular la distancia entre dos cargas en un sistema de coordenadas x, y, z
def calc_distancia(x1, y1, z1, x2, y2, z2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)

# Obtener entrada del usuario para la elección del sistema de unidades
sistema = input("Introduzca el sistema de unidades (Coulombs o microcoulombs): ")

# Obtener entrada del usuario para el número de cargas
num_cargas = int(input("Introduzca el número de cargas: "))

# Crear una lista para almacenar las cargas y sus posiciones
cargas = []
for i in range(num_cargas):
    # Obtener entrada del usuario para la carga y sus coordenadas x, y, z
    carga = float(input(f"Introduzca la carga {i+1}: "))
    x = float(input(f"Introduzca la posición x de la carga {i+1}: "))
    y = float(input(f"Introduzca la posición y de la carga {i+1}: "))
    z = float(input(f"Introduzca la posición z de la carga {i+1}: "))
    cargas.append((carga, x, y, z))

# Obtener entrada del usuario para la elección de dos cargas para calcular la distancia entre ellas
opcion = input("Seleccione una opción: \n1. Calcular fuerza electrostática entre dos cargas \n2. Calcular distancia entre dos cargas \nOpción: ")
if opcion == "1":
    # Obtener entrada del usuario para seleccionar dos cargas para calcular la fuerza electrostática
    carga1 = int(input("Seleccione la carga 1: "))
    carga2 = int(input("Seleccione la carga 2: "))
    
    # Calcular la distancia entre las dos cargas seleccionadas
    q1, x1, y1, z1 = cargas[carga1-1]
    q2, x2, y2, z2 = cargas[carga2-1]
    distancia = calc_distancia(x1, y1, z1, x2, y2, z2)
    
    # Calcular la fuerza electrostática entre las dos cargas seleccionadas
    fuerza = calc_fuerza_electrostatica(q1, q2, distancia)
    
    # Determinar si es una fuerza de atracción o de repulsión
    if q1 * q2 > 0:
        tipo_fuerza = "repulsion"
    else:
        tipo_fuerza = "atracción"
    
    # Mostrar el resultado
    print(f"La distancia entre la carga {carga1} y la carga {carga2} es {distancia} unidades.")
    print(f"La fuerza electrostática entre la carga {carga1} y la carga {carga2} es {fuerza} {sistema}.")
    print(f"La fuerza es una fuerza de {tipo_fuerza}.")

    # Dibujar la gráfica de las cargas
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x1, y1, z1, c='red', marker='o')
    ax.scatter(x2, y2, z2, c='blue', marker='o')
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')
    plt.show()
    
elif opcion == "2":
    # Obtener entrada del usuario para seleccionar dos cargas para calcular la distancia entre ellas
    carga1 = int(input("Seleccione la carga 1: "))
    carga2 = int(input("Seleccione la carga 2: "))
    
    # Calcular la distancia entre las dos cargas seleccionadas
    q1, x1, y1, z1 = cargas[carga1-1]
    q2, x2, y2, z2 = cargas[carga2-1]
    distancia = calc_distancia(x1, y1, z1, x2, y2, z2)
    
    # Calcular la fuerza electrostática entre las dos cargas seleccionadas
    fuerza = float(input(f"Introduzca la fuerza electrostática entre la carga {carga1} y la carga {carga2}: "))
    
    # Calcular la distancia entre las dos cargas a partir de la fuerza electrostática
    distancia = math.sqrt(k * q1 * q2 / fuerza)
    
    # Mostrar el resultado
    print(f"La distancia entre la carga {carga1} y la carga {carga2} es {distancia} unidades.")
    
    # Dibujar la gráfica de las cargas
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x1, y1, z1, c='red', marker='o')
    ax.scatter(x2, y2, z2, c='blue', marker='o')
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')
    plt.show()
    
else:
    print("Opción inválida.")

