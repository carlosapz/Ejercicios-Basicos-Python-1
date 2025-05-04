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
sistema = input("Introduzca los datos en el sistema de unidades de Coulombs: ")

# Obtener entrada del usuario para el número de cargas
num_cargas = int(input("Introduzca el número de cargas: "))

# Crear una lista para almacenar las cargas y sus posiciones
cargas = []
cargas_verdes = []
for i in range(num_cargas):
    # Obtener entrada del usuario para la carga y sus coordenadas x, y, z
    carga = float(input(f"Introduzca la carga {i+1}: "))
    x = float(input(f"Introduzca la posición x de la carga {i+1}: "))
    y = float(input(f"Introduzca la posición y de la carga {i+1}: "))
    z = float(input(f"Introduzca la posición z de la carga {i+1}: "))
    cargas.append((carga, x, y, z))
    if input(f"¿Desea incluir la carga {i+1} en el cálculo de la fuerza? (s/n): ") == "s":
        cargas_verdes.append(i)

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
        print(f"La distancia entre la carga {carga1} y la carga 2 {carga2} es de {distancia} metros.")
        print(f"La fuerza electrostática entre la carga {carga1} y la carga {carga2} es de {fuerza} newtons y es una fuerza de {tipo_fuerza}.")

elif opcion == "2":
    # Obtener entrada del usuario para seleccionar dos cargas para calcular la distancia
    carga1 = int(input("Seleccione la carga 1: "))
    carga2 = int(input("Seleccione la carga 2: "))
    # Calcular la distancia entre las dos cargas seleccionadas
    q1, x1, y1, z1 = cargas[carga1-1]
    q2, x2, y2, z2 = cargas[carga2-1]
    distancia = calc_distancia(x1, y1, z1, x2, y2, z2)

    # Mostrar el resultado
    print(f"La distancia entre la carga {carga1} y la carga {carga2} es de {distancia} metros.")
else:
    print("Opción no válida. Por favor seleccione una opción válida.")

