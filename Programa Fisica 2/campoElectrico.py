import math
import matplotlib.pyplot as plt

# Función para calcular el campo eléctrico debido a una carga puntual
def calc_campo_electrico_puntual(q, r, x, y, z):
    k = 9e9
    dx = x - r[0]
    dy = y - r[1]
    dz = z - r[2]
    r = math.sqrt(dx*dx + dy*dy + dz*dz)
    e = k * q / (r*r)
    
    ex = e * dx / r
    ey = e * dy / r
    ez = e * dz / r
    return [ex, ey, ez]

# Función para calcular el campo eléctrico debido a una distribución discreta de cargas
def calc_campo_electrico_distribucion(q, r, x, y, z):
    e_total = [0, 0, 0]
    for i in range(len(q)):
        e_puntual = calc_campo_electrico_puntual(q[i], r[i], x, y, z)
        e_total[0] += e_puntual[0]
        e_total[1] += e_puntual[1]
        e_total[2] += e_puntual[2]
    return e_total

# Función para graficar el campo eléctrico en un plano x, y, z
def graficar_campo_electrico(q, r, x_min, x_max, y_min, y_max, z_min, z_max, nx, ny, nz):
    xs = [x_min + i*(x_max-x_min)/(nx-1) for i in range(nx)]
    ys = [y_min + i*(y_max-y_min)/(ny-1) for i in range(ny)]
    zs = [z_min + i*(z_max-z_min)/(nz-1) for i in range(nz)]
    e_x = [[0 for j in range(ny)] for i in range(nx)]
    e_y = [[0 for j in range(ny)] for i in range(nx)]
    e_z = [[0 for j in range(ny)] for i in range(nx)]
    for i in range(nx):
        for j in range(ny):
            for k in range(nz):
                e = calc_campo_electrico_distribucion(q, r, xs[i], ys[j], zs[k])
                e_x[i][j] += e[0]
                e_y[i][j] += e[1]
                e_z[i][j] += e[2]
    fig, axs = plt.subplots(3, sharex=True, sharey=True)
    fig.suptitle('Campo eléctrico')
    axs[0].contourf(xs, ys, e_x, cmap='plasma')
    axs[0].set_ylabel('y')
    axs[1].contourf(xs, ys, e_y, cmap='plasma')
    axs[1].set_ylabel('y')
    axs[2].contourf(xs, ys, e_z, cmap='plasma')
    axs[2].set_ylabel('y')
    for ax in axs:
        ax.set_xlabel('x')
    plt.show()

# Función principal para ejecutar el programa
def main():
    # Pedir al usuario que introduzca los datos del sistema
    sistema = input("Introduce el sistema de unidades (Coulombs, microCoulombs, etc.): ")
    
    # Pedir al usuario que introduzca los datos de la distribución de carga discreta
    n = int(input("Introduce el número de cargas: "))
    q = []
    r = []
    for i in range(n):
        q_i = float(input("Introduce la carga de la carga " + str(i+1) + " en " + sistema + ": "))
        x_i = float(input("Introduce la posición x de la carga " + str(i+1) + " en metros: "))
        y_i = float(input("Introduce la posición y de la carga " + str(i+1) + " en metros: "))
        z_i = float(input("Introduce la posición z de la carga " + str(i+1) + " en metros: "))
        q.append(q_i)
        r.append([x_i, y_i, z_i])
    
    # Pedir al usuario que elija una operación
    operacion = None
    while operacion not in ['1', '2', '3']:
        print("Elige una operación:")
        print("1. Calcular el campo eléctrico en un punto")
        print("2. Graficar el campo eléctrico en un plano")
        print("3. Salir")
        operacion = input("> ")
    
    # Realizar la operación elegida por el usuario
    if operacion == '1':
        x = float(input("Introduce la posición x del punto en metros: "))
        y = float(input("Introduce la posición y del punto en metros: "))
        z = float(input("Introduce la posición z del punto en metros: "))
        e = calc_campo_electrico_distribucion(q, r, x, y, z)
        print("El campo eléctrico en el punto (" + str(x) + ", " + str(y) + ", " + str(z) + ") es (" + str(e[0]) + ", " + str(e[1]) + ", " + str(e[2]) + ") " + sistema + "/metro")
    elif operacion == '2':
        x_min = float(input("Introduce la posición x mínima del plano en metros: "))
        x_max = float(input("Introduce la posición x máxima del plano en metros: "))
        y_min = float(input("Introduce la posición y mínima del plano en metros: "))
        y_max = float(input("Introduce la posición y máxima del plano en metros: "))
        z_min = float(input("Introduce la posición z mínima del plano en metros: "))
        z_max = float(input("Introduce la posición z máxima del plano en metros: "))
        nx = int(input("Introduce el número de puntos en la dirección x: "))
        ny = int(input("Introduce el número de puntos en la dirección y: "))
        nz = int(input("Introduce el número de puntos en la dirección z: "))
        graficar_campo_electrico(q, r, x_min, x_max, y_min, y_max, z_min, z_max, nx, ny, nz)

if __name__ == '__main__':
    main()
