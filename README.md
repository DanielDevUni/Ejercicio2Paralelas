# 🚀 Comparación de Suma de Vectores en Python

Este proyecto implementa dos versiones de un programa que suma los elementos de un vector muy grande (100,000,000 elementos):

1. **Versión con Multiprocessing** (paralelismo en múltiples procesos).  
2. **Versión con NumPy** (vectorización SIMD).

El objetivo es comparar tiempos de ejecución, calcular el **speedup**, la **eficiencia** y el **factor de mejora** entre ambas versiones.

---

## 📂 Estructura del repositorio
- `sum_procesos.py` → versión con multiprocessing.  
- `sum_numpy.py` → versión con NumPy.  
- `README.md` → documentación, resultados y conclusiones.  

---

## ⚙️ Ejecución
### Multiprocessing
```bash
python sum_procesos.py
```

### Numpy
```bash
python sum_numpy.py
```

---

## 📊 Resultados

### Tiempos de ejecución (segundos)

| Procesos | Tiempo Promedio (seg) |
|----------|------------------------|
| 1        | 0,9207                 |
| 2        | 0,7255                 |
| 4        | 0,7444                 |
| 8        | 0,8755                 |

---

### Speedup y Eficiencia (Multiprocessing)



$S_p = \frac{T_1}{T_p}, \quad E_p = \frac{S_p}{p}$



| Procesos | Tiempo Promedio (seg) | Speedup | Eficiencia |
|----------|------------------------|---------|------------|
| 1        | 0,9207                 | 1,0000  | -          |
| 2        | 0,7255                 | 1,2691  | 63,5%      |
| 4        | 0,7444                 | 1,2368  | 30,9%      |
| 8        | 0,8755                 | 1,0516  | 13,1%      |

---

### Comparación Multiprocessing vs NumPy



$F = \frac{T_{\text{procesos}}}{T_{\text{numpy}}}$




| Versión                     | Tiempo Promedio (seg) | Factor de mejora |
|-----------------------------|------------------------|------------------|
| Multiprocessing (1 proceso) | 0,9207                 | 12,07            |
| NumPy                       | 0,0763                 | -                |

---

## 📝 Observaciones y Conclusiones

- El tiempo secuencial (1 proceso) fue de **0,9207 seg**.  
- Con 2 procesos se obtuvo un **speedup de 1,27** y una eficiencia de **63,5%**, lo que muestra cierta mejora.  
- Al aumentar a 4 y 8 procesos, la eficiencia cayó drásticamente (30,9% y 13,1%), evidenciando el **overhead** de crear y coordinar procesos.  
- La versión con **NumPy** fue la más rápida: **0,0763 seg**, aproximadamente **12 veces más veloz** que la versión secuencial con procesos.  
- Esto confirma que la **vectorización SIMD** de NumPy es mucho más eficiente que el paralelismo con procesos para este tipo de operaciones.  
- Conclusión: **NumPy es la mejor opción** para sumar grandes vectores en Python, ya que aprovecha optimizaciones internas y reduce el costo de comunicación entre procesos. 
