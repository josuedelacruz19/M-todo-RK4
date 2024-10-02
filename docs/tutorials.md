# Ejemplo de Uso

En este tutorial, se ejemplifica como se implementa y ejecuta el método RK4 para resolver el problema dinámico especificado. Utilizamos un ejemplo específico donde \( f(t, y) = -i[O, y(t)] \) y generamos un gráfico para visualizar los resultados.


```python
import numpy as np
import matplotlib.pyplot as plt

# Matriz de operación
O = np.array([[0, -1j], [1j, 0]])

# Estado inicial
y0 = np.array([[1+0j, 0], [0, 0]])

# Parámetros de tiempo
t_min = 0
t_max = 10
steps = 100

# Simulación
times, stateQuant00, stateQuant11 = simulate_dynamics(O, y0, t_min, t_max, steps)

# Graficar resultados
plt.plot(times, stateQuant00, label='Estado (0,0)')
plt.plot(times, stateQuant11, label='Estado (1,1)')
plt.xlabel('Tiempo')
plt.ylabel('Valor real de las entradas')
plt.legend()
plt.show()
