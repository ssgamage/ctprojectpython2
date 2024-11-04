import sympy as sp
from django.shortcuts import render

from .numerical_methods import (bisection_method, newton_raphson_method,
                                secant_method)


# Function to parse and convert user input into a sympy function
def parse_function(func_str):
    x = sp.symbols('x')  # Declare 'x' as the variable
    try:
        return sp.sympify(func_str)
    except (sp.SympifyError, SyntaxError):
        return None

def index(request):
    return render(request, 'solver/index.html')

def bisection(request):
    if request.method == 'POST':
        func_str = request.POST['function']
        a = float(request.POST['a'])
        b = float(request.POST['b'])
        tol = float(request.POST['tolerance'])
        max_iter = int(request.POST['max_iter'])
        
        # Parse the user function
        f_sympy = parse_function(func_str)
        if f_sympy is None:
            return render(request, 'solver/error.html', {'error': 'Invalid function syntax'})
        
        # Convert to a Python function
        f = sp.lambdify(sp.symbols('x'), f_sympy)
        
        # Call your bisection method
        root, iterations, error = bisection_method(f, a, b, tol, max_iter)
        return render(request, 'solver/result.html', {'method': 'Bisection', 'root': root, 'iterations': iterations, 'error': error})
    
    return render(request, 'solver/bisection.html')

def newton_raphson(request):
    if request.method == 'POST':
        func_str = request.POST['function']
        derivative_str = request.POST['derivative']
        x0 = float(request.POST['initial_guess'])
        tol = float(request.POST['tolerance'])
        max_iter = int(request.POST['max_iter'])
        
        # Parse the user function and its derivative
        f_sympy = parse_function(func_str)
        df_sympy = parse_function(derivative_str)
        if f_sympy is None or df_sympy is None:
            return render(request, 'solver/error.html', {'error': 'Invalid function or derivative syntax'})
        
        # Convert to Python functions
        f = sp.lambdify(sp.symbols('x'), f_sympy)
        df = sp.lambdify(sp.symbols('x'), df_sympy)
        
        # Call your Newton-Raphson method
        root, iterations, error = newton_raphson_method(f, df, x0, tol, max_iter)
        return render(request, 'solver/result.html', {'method': 'Newton-Raphson', 'root': root, 'iterations': iterations, 'error': error})
    
    return render(request, 'solver/newton_raphson.html')

def secant(request):
    if request.method == 'POST':
        func_str = request.POST['function']
        x0 = float(request.POST['initial_guess1'])
        x1 = float(request.POST['initial_guess2'])
        tol = float(request.POST['tolerance'])
        max_iter = int(request.POST['max_iter'])
        
        # Parse the user function
        f_sympy = parse_function(func_str)
        if f_sympy is None:
            return render(request, 'solver/error.html', {'error': 'Invalid function syntax'})
        
        # Convert to a Python function
        f = sp.lambdify(sp.symbols('x'), f_sympy)
        
        # Call your Secant method
        root, iterations, error = secant_method(f, x0, x1, tol, max_iter)
        return render(request, 'solver/result.html', {'method': 'Secant', 'root': root, 'iterations': iterations, 'error': error})
    
    return render(request, 'solver/secant.html')
