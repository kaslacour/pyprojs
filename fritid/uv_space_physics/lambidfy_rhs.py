# derive 2d riemannian geodesic equations
import sympy as sp
from sympy import Matrix,  zeros, symbols, trigsimp, cos, sin, oo
from sympy import Function, Symbol
from sympy import lambdify
from sympy.utilities.lambdify import lambdastr
from sympy.physics.vector import dynamicsymbols
from sympy.concrete.summations import Sum
from numpy import sqrt

x0,x1 = symbols('x:2')

def lambda_rhs(diffeo = Matrix([cos(x1)*cos(x0), cos(x1)*sin(x0), sin(x1)]), manifoldName = "default_manifold"):
    x = Matrix([x0,x1])
    Jx = diffeo.jacobian(x)
    metric_matrix = trigsimp(Jx.T * Jx)
    metric_matrix_inverted = trigsimp(metric_matrix.inv())
    christoffel_symbols = (sp.zeros(2,2), sp.zeros(2,2))
    for m in range(2):
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    christoffel_symbols[m][i,j] += 1/2 * metric_matrix_inverted[k,m] * \
                    (sp.diff(metric_matrix[i,k],x[j]) + sp.diff(metric_matrix[j,k],x[i]) - sp.diff(metric_matrix[i,j],x[k]))


    for m, aisle in enumerate(christoffel_symbols):
        for i in range(2):
            for j in range(2):
                christoffel_symbols[m][i,j] = trigsimp(christoffel_symbols[m][i,j])

    # d^2x^i/dt^2 = - sum(L^i_{jk} * dx^j/dt * x^k/dt)
    j,k = symbols('j,k')
    # c = dynamicsymbols('c:2')
    y = symbols('y:2')
    y0,y1 = y
    rhs = [0]*4
    for i in range(2):
        for j in range(2):
            for k in range(2):
                rhs[2+i] -= christoffel_symbols[i][j,k] * y[j] * y[k]
    rhs[0:2] = y[:]
    for i in range(2):
        rhs[i] = trigsimp(rhs[i])


    # u-coordinate: x0
    # v-coordinate: x1
    # u-speed:      dx0/dt = y0
    # v-speed:      dx1/dt = y1

    # dy0/dt = y0
    # dy1/dt = y1
    # dy2/dt =       
    # dy3/dt = 
    #print(lambdastr([y],rhs))
    lam_rhs = str(rhs)
    return lam_rhs


