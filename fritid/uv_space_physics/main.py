from scipy.integrate import solve_ivp
import numpy as np
import sympy as sp
from sympy import Matrix,  zeros, symbols, trigsimp, cos, sin, oo
from sympy import Function, Symbol
from sympy import lambdify
from sympy.utilities.lambdify import lambdastr
from sympy.physics.vector import dynamicsymbols
from sympy.concrete.summations import Sum


# parameterisation of a sphere, with -pi<x[0]<pi, -pi/2<x[1]<pi/2
'''
diffeo = lambda x : np.array([np.cos(x[1])*np.cos(x[0]),
                              np.cos(x[1])*np.cos(x[1])],
                              np.sin([x[1]]))
'''
x0,x1 = symbols('x:2')
diffeo = Matrix([cos(x1)*cos(x0), cos(x1)*sin(x0), sin(x1)])
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
y = symbols('y:4')
rhs = [0]*4
for i in range(2):
    for j in range(2):
        for k in range(2):
            rhs[2+i] -= christoffel_symbols[i][j,k] * y[2+j] * y[2+k]
rhs[0:2] = y[2:]
for i in range(2):
    rhs[i] = trigsimp(rhs[i])


# x0 -> y0
# x1 -> y1
# dx0/dt -> y2
# dx1/dt -> y3

# dy0/dt = y2
# dy1/dt = y3
# dy2/dt = 
# dy3/dt = 
print(lambdastr(y,rhs))
lam_rhs = lambdify(y, rhs)

# TODO: if the amount of operations in the symbolic derived rhs of the system of differential equations is too great
# use a purely numerical scheme instead



def vec(*args):
    return np.array(args, dtype=np.float32)
def rhs(t : np.float32, y : np.float32, ):
    # dy/dt = -2y * t




    pass

def main():
    #y0 = vec(1.0,2.0)
    #t = np.float32(1)
    #sol = solve_ivp(rhs,[0,t],y0)




    pass
if __name__ == "__main__":
    main()