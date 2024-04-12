def euler(f, x0, y0, h, n):
    """
    Implementación del método de Euler para resolver una ecuación diferencial ordinaria de primer orden.
    
    Parámetros:
    f: Función que representa la ecuación diferencial dy/dx = f(x, y).
    x0: Valor inicial de x.
    y0: Valor inicial de y.
    h: Tamaño del paso.
    n: Número de pasos.
    
    Devuelve:
    Una lista con las aproximaciones de la solución y(x) en cada punto.
    """
    x_values = [x0]
    y_values = [y0]
    
    for i in range(n):
        x = x_values[-1]
        y = y_values[-1]
        
        y_next = y + h * f(x, y)
        x_next = x + h
        
        x_values.append(x_next)
        y_values.append(y_next)
    
    return x_values, y_values

def f(x, y):
    return 2 * x  # Ejemplo de ecuación diferencial dy/dx = 2x

x0 = 0  # Valor inicial de x
y0 = 1  # Valor inicial de y
h = 0.1  # Tamaño del paso
n = 10  # Número de pasos

x_values, y_values = euler(f, x0, y0, h, n)

for x, y in zip(x_values, y_values):
    print(f"x = {x}, y = {y}")