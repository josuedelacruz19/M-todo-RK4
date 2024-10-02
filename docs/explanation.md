# Método RK4 (Explanation)

El método de Runge-Kutta de cuarto orden (RK4) es un método numérico para resolver ecuaciones diferenciales ordinarias de la forma:

$$ \frac{dy}{dt} = f(t, y) $$

Cada iteración del método RK4 se resuelve conforme:

1. Se calcula \( k_{1} = hf(t_{n}, y_{n}) \)
2. Se calcula \( k_{2} = hf(t_{n} + \frac{h}{2}, y_{n} + \frac{k_{1}}{2}) \)
3. Se calcula \( k_{3} = hf(t_{n} + \frac{h}{2}, y_{n} + \frac{k_{2}}{2}) \)
4. Se calcula \( k_{4} = hf(t_{n} + h, y_{n} + k_{3}) \)
5. Finalmente se actualiza \( y_{n+1} = y_{n} + \frac{1}{6}(k_{1} + 2k_{2} + 2k_{3} + k_{4}) \)

Este método utiliza cuatro puntos intermedios para calcular el valor \( y_{n+1} \), lo que proporciona una mayor presición respecto a métodos sencillos como Euler.
