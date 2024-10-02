# Reference page for module 'RK4'

```markdown
# Referencia de Funciones

Esta sección detalla las funciones utilizadas en el documento. Las dos funciones principales son `dyn_generator()`y `rk4()`.

## dyn_generator(O, y)
Genera la dinámica del sistema.

### Parámetros:
- `O` : Matriz de operación.
- `y` : Estado actual del sistema.

### Retorno:
- Devuelve el resultado de la multiplicación matricial entre `O` y `y`.

### Ejemplo de uso:

```python
O = np.array([[0, -1j], [1j, 0]])
y = np.array([1, 0])
dyn_generator(O, y)


::: RK4.RK4
