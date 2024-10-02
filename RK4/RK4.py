import numpy as np

def dyn_generator(O, y):
    """
    Genera la dinámica del sistema según la ecuación diferencial dada.

    La función calcula -i[O, y], donde O es una matriz de operación y y es el estado actual del sistema.

    Parámetros:

    -----------

    O : numpy.ndarray
        Matriz de operación.

    y : numpy.ndarray
        Estado actual del sistema.


    Retorno:

    --------

    numpy.ndarray
        El resultado de la operación -i[O, y].


    Ejemplo de uso:

    ---------------

    >>> O = np.array([[0, -1j], [1j, 0]])
    >>> y = np.array([1, 0])
    >>> dyn_generator(O, y) array([0.-1.j, 0.+1.j])

    """

    return -1j * np.dot(0, y)


def rk4(function, oper, state, h):
    """

    Método de Runge-Kutta de cuarto orden (RK4) para resolver una ecuación diferencial ordinaria (EDO).

    La función aproxima la solución de la EDO de la forma dy/dt = f(t, y) utilizando un paso temporal h.

    Parámetros:
    ------------

    state : numpy.ndarray 
            El estado actual del sistema y.
    function : function
               La función que describe la dinámica del sistema (es decir, dy/dt = f(t, y)).
    oper : float
           t, el tiempo actual.
    h : float
        El paso del tiempo.

    Retorno:
    ---------

    numpy.ndarray 
        El nuevo estado del sistema tras el paso de integración.

    Ejemplo de uso:
    ----------------

    >>> O = np.array([[0, -1j], [1j, 0]])
    >>> y0 = np.array([1, 0])
    >>> f = lambda t, y: dyn_generator(O, y)
    >>> t0 = 0
    >>> h = 0.1
    >>> rk4(y0, f, t0, h)
    array([0.99500417-0.09983342j, 0.09983342+0.99500417j])
    """
    runge_k1 = h * function(oper, state)
    runge_k2 = h * function(oper, state + (runge_k1/2))
    runge_k3 = h * function(oper, state + (runge_k2/2))
    runge_k4 = h * function(oper, state + runge_k3)

    return state + (1/6) * (runge_k1 + ( 2 * runge_k2) + ( 2 * runge_k3) + runge_k4)

def simulate_dynamics(O, y0, t_min, t_max, steps):
    """
    Simula la dinámica temporal de un sistema utilizando el método RK4.

    Parámetros:
    -----------
    O : numpy.ndarray
        Matriz de operación que define la dinámica del sistema.
    y0 : numpy.ndarray
        Estado inicial del sistema.
    t_min : float
        Tiempo inicial de la simulación.
    t_max : float
        Tiempo final de la simulación.
    steps : int
        Número de pasos de tiempo.

    Retorno:
    --------
    times : numpy.ndarray
        Arreglo con los tiempos simulados.
    stateQuant00 : numpy.ndarray
        Arreglo con los valores de la entrada (0,0) del estado en cada paso de tiempo.
    stateQuant11 : numpy.ndarray
        Arreglo con los valores de la entrada (1,1) del estado en cada paso de tiempo.
    """
    # Crear un arreglo de tiempos
    times = np.linspace(t_min, t_max, steps)
    h = (t_max - t_min) / steps

    # Inicializar el estado y los arreglos para guardar las cantidades de interés
    yCopy = yInit.copy()

    stateQuant00 = np.zeros(times.size)
    stateQuant11 = np.zeros(times.size)

    # Definir la función de dinámica
    f = lambda t, y: dyn_generator(O, y)

    # Iterar sobre los tiempos y aplicar RK4
    for tt in range(times.size):
        # Guardar los valores reales de las entradas (0,0) y (1,1) del estado
        stateQuant00[tt] = yCopy[0, 0].real
        stateQuant11[tt] = yCopy[1, 1].real

        # Actualizar el estado usando el método RK4
        yN = rk4(yCopy, f, times[tt], h)
        yCopy = yInit.copy(yN)

    return times, stateQuant00, stateQuant11
