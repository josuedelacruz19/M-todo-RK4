# Introducción: Método de Runge-Kutta de cuarto orden (RK4)

Este documento se centra en la resolución numérica de un problema dinámico utilizando el método Runge-Kutta de cuarto orden (RK4). Se busca resolver la ecuación diferencial ordinaria (EDO) de la forma:
 
\[
\frac{dy}{dt} = f(t, y)
\]

donde se tiene la siguiente condición inicial: \( y(t_{0}) = y_{0} \). Se utiliza la metodología RK4 debido a su precisión y estabilidad.

En este ejemplo, se considera un problema específico en el cual \( f(t, y) = -i[O, y(t)] \), donde no hay dependencia temporal explícita en la función \( f(t, y) \).
 
El módulo se encuentra en:

[github.com](https://github.com/josuedelacruz19/M-todo-RK4)
