from sympy import symbols, diff, integrate, solve, Eq, sin, cos, simplify

x, y = symbols('x y')
expr = sin(x)**2 + cos(x)**2
simplified_expr = simplify(expr)
print(f"Simplified expression: {simplified_expr}")

