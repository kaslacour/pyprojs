
from sympy import diff, Symbol, symbols
from sympy.vector import CoordSys3D, Vector
from sympy import exp


x = symbols('x(0:2)')
y = symbols('y(0:3)')

diffeo = lambda x : (x[0],x[1],exp(-x[0]**2-x[1]**2))





