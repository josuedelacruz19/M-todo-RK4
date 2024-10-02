# Referencia de Funciones

Esta sección detalla las funciones utilizadas en el documento. 

## `dyn_generator(operador, Init_state)`

Genera el valor de la función $$ f(t, y) $$ para el sistema dado.

### Parámetros
- `operador` (ndarray): Matriz de operación.
- `Init_state` (ndarray): Estado inicial del sistema.

### Retorno
- ndarray: Devuelve el resultado de la operación $$ -i[O, y(t)] $$.

### Ejemplo
```python
oOper = np.array([[0, 1], [1, 0]])
yInit = np.array([[1, 0], [0, 0]])
resultado = dyn_generator(oOper, yInit)
print(resultado)



::: RK4.RK4
