# solver/numerical_methods.py

def bisection_method(f, a, b, tol, max_iter):
    if f(a) * f(b) >= 0:
        raise ValueError("The function must have different signs at endpoints a and b.")

    iter_count = 0
    c = a
    while (b - a) / 2 > tol and iter_count < max_iter:
        c = (a + b) / 2
        if f(c) == 0:
            break
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
        iter_count += 1
    
    final_error = abs(b - a) / 2
    return c, iter_count, final_error

# solver/numerical_methods.py

def newton_raphson_method(f, df, x0, tol, max_iter):
    iter_count = 0
    x = x0
    while abs(f(x)) > tol and iter_count < max_iter:
        x = x - f(x) / df(x)
        iter_count += 1
    
    final_error = abs(f(x))
    return x, iter_count, final_error


# solver/numerical_methods.py

def secant_method(f, x0, x1, tol, max_iter):
    iter_count = 0
    while abs(f(x1)) > tol and iter_count < max_iter:
        try:
            x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        except ZeroDivisionError:
            raise ValueError("Division by zero encountered in secant method.")
        
        x0, x1 = x1, x2
        iter_count += 1
    
    final_error = abs(f(x1))
    return x1, iter_count, final_error
