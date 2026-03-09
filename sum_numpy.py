import numpy as np
import time

def ejecutar_numpy(N):
    datos = np.ones(N, dtype=np.int32)

    inicio = time.perf_counter()
    total = np.sum(datos)
    fin = time.perf_counter()

    return total, fin - inicio

if __name__ == "__main__":
    N = 100_000_000

    tiempos = []
    for i in range(5):
        _, t = ejecutar_numpy(N)
        tiempos.append(t)
        print(f"Numpy, Ejecución {i+1}: {t:.4f} seg")

    tiempos.sort()
    tiempos_prom = sum(tiempos[1:-1]) / 3
    print(f"Numpy, Tiempo promedio (sin extremos): {tiempos_prom:.4f} seg\n")
