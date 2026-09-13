import numpy as np
np.set_printoptions(precision=6, suppress=True)

def imprimir_matriz(nombre, M):
    print(f"\n{nombre} =")
    filas = ["A", "B", "C"]
    for etiqueta, fila in zip(filas, M):
        valores = "  ".join(f"{v:10.6f}" for v in fila)
        print(f"  {etiqueta}: {valores}")


def main():
    # Matriz de transicion 
    P = np.array([
        [0.5, 0.0, 0.5],
        [0.0, 0.5, 0.5],
        [0.5, 0.5, 0.0],
    ])

    x0 = np.array([100.0, 200.0, 300.0])

    imprimir_matriz("P", P)

    # Cuadrados sucesivos: P^2, P^4, P^8, P^16
    P2 = P @ P
    imprimir_matriz("P^2 = P * P", P2)

    P4 = P2 @ P2
    imprimir_matriz("P^4 = P^2 * P^2", P4)

    P8 = P4 @ P4
    imprimir_matriz("P^8 = P^4 * P^4", P8)

    P16 = P8 @ P8
    imprimir_matriz("P^16 = P^8 * P^8", P16)

    # P^24 = P^16 * P^8
    P24 = P16 @ P8
    imprimir_matriz("P^24 = P^16 * P^8", P24)

    # Distribucion de toneladas a los 24 meses
    x24 = P24 @ x0
    print(f"\nVector inicial x0 = {x0}")
    print(f"Distribucion a los 24 meses = {x24}")

if __name__ == "__main__":
    main()