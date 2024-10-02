# Tutorial: Uso del Método RK4

En este tutorial, se mostrará cómo utilizar el método de Runge-Kutta de cuarto orden (RK4) para resolver un problema dinámico.

## Paso 1: Importar Bibliotecas

Primero, se importan las bibliotecas necesarias:

```python
import numpy as np
import matplotlib.pyplot as plt
```

## Paso 2: Definir Parámetros Iniciales


```python
# Definimos el operador como una matriz
oOper = np.array([[0, 1], [1, 0]])

# Estado inicial (ejemplo)
yInit = np.array([[1, 0], [0, 0]])

# Paso de tiempo
h = 0.1

# Tiempo total de simulación
t_total = 10
times = np.arange(0, t_total, h)

# Inicializar el estado copia
yCopy = yInit.copy()
```

## Paso 3: Crear Arreglos para Almacenar Resultados

Inicializar arreglos para almacenar los resultados de las entradas (0,0) y (1,1):

```python
# Arreglos para almacenar los valores de las entradas (0,0) y (1,1)
stateQuant00 = np.zeros(times.size)
stateQuant11 = np.zeros(times.size)
```

## Paso 4: Bucle de Simulación

Implementación  del bucle `for` para calcular la dinámica temporal utilizando el método RK4:

```python
for tt in range(times.size):
    # Guardar el valor de las entradas (0,0) y (1,1) en los arreglos
    stateQuant00[tt] = yCopy[0, 0].real
    stateQuant11[tt] = yCopy[1, 1].real

    # Invocar rk4 operando sobre yInit
    yN = rk4(dyn_generator, oOper, yCopy, h)

    # Ahora asignamos yN a yCopy para la próxima iteración
    yCopy = yN
```

## Paso 5: Graficar Resultados

Finalmente, se grafican los resultados almacenados en los arreglos:

```python
plt.figure(figsize=(10, 5))
plt.plot(times, stateQuant00, label='Estado (0,0)', color='b')
plt.plot(times, stateQuant11, label='Estado (1,1)', color='r')
plt.title('Evolución de los Estados a lo largo del Tiempo')
plt.xlabel('Tiempo')
plt.ylabel('Valores de Estado')
plt.legend()
plt.grid()
plt.show()
```
