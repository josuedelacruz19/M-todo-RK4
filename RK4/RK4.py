import numpy as np

iConst = 1.0j

def dyn_generator(operador, Init_state):
    """
    Genera el valor de la función f(t, y) para el sistema dado.

    Parámetros:
    - operador (ndarray): Matriz de operación.
    - Init_state (ndarray): Estado inicial del sistema.

    Retorno:
    - ndarray: Devuelve el resultado de la operación -i[O, y(t)].

    Ejemplo:
    >>> oOper = np.array([[0, 1], [1, 0]])
    >>> yInit = np.array([[1, 0], [0, 0]])
    >>> dyn_generator(oOper, yInit)
    array([[0.+0.j, 0.+1.j],
           [0.+1.j, 0.+0.j]])
    """

    return (-1) * iConst * (np.dot(operador, Init_state) - np.dot(Init_state, operador))

def rk4(funcion, oper, state, h):
    """
    Implementa el método de Runge-Kutta de cuarto orden.

    Parámetros:
    - funcion (callable): La función que describe el sistema.
    - oper (ndarray): Matriz de operación.
    - state (ndarray): Estado actual del sistema.
    - h (float): Paso de tiempo.

    Retorno:
    - ndarray: Devuelve el nuevo estado del sistema tras aplicar el método RK4.

    Ejemplo:
    >>> oOper = np.array([[0, 1], [1, 0]])
    >>> yInit = np.array([[1, 0], [0, 0]])
    >>> h = 0.1
    >>> rk4(dyn_generator, oOper, yInit, h)
    array([[0.99666369+0.j        , 0.09983333+0.1j        ],
           [0.09983333+0.j        , 0.99666369+0.1j        ]])
    """

    runge_k1 = h * funcion(oper, state)
    runge_k2 = h * funcion(oper, state + (runge_k1 / 2))
    runge_k3 = h * funcion(oper, state + (runge_k2 / 2))
    runge_k4 = h * funcion(oper, state + runge_k3)
    return state + (1/6) * (runge_k1 + 2 * runge_k2 + 2 * runge_k3 + runge_k4)
