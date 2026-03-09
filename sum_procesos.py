import multiprocessing as mp
import numpy as np
import time

def suma_parcial(datos):
    return np.sum(datos)

def ejecutar(n_procesos, datos):
    # Dividir el arreglo en partes iguales
    partes = np.array_split(datos, n_procesos)

    inicio = time.perf_counter()

    with mp.Pool(processes=n_procesos) as pool:
        resultados = pool.map(suma_parcial, partes)

    total = sum(resultados)
    fin = time.perf_counter()

    return total, fin - inicio

if __name__ == "__main__":
    N = 100_000_000
    datos = np.ones(N, dtype=np.int32)  # arreglo gigante de unos

    for p in [1, 2, 4, 8]:
        tiempos = []
        for i in range(5):
            _, t = ejecutar(p, datos)
            tiempos.append(t)
            print(f"Procesos={p}, Ejecución {i+1}: {t:.4f} seg")

        # eliminar el mayor y el menor
        tiempos.sort()
        tiempos_prom = sum(tiempos[1:-1]) / 3
        print(f"Procesos={p}, Tiempo promedio (sin extremos): {tiempos_prom:.4f} seg\n")
