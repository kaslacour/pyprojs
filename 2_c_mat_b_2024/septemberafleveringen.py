from sympy.parsing.sympy_parser import parse_expr
from sympy import expand, Subs, Symbol, S
from sympy import solveset
import matplotlib.pyplot as plt
import numpy as np

def print_exercise_with_solution(expr: str, **kwargs,) -> str:

    sol = expand(parse_expr(expr,transformations='all'))
    if kwargs:
        sol = Subs(sol,kwargs["vars"],kwargs["values"])
        sol = sol.doit()
    sol = str(sol)
    sol = sol.replace("**", "^")
    print(str(expr).replace("**","^"),"=",sol)

#import sys
#with open('facit.txt','w') as f:
#    sys.stdout = f

def opgave1():
    #Opgave 1
    print("===Opgave 1====")
    f = lambda x : 2*x+3
    print(f"f(x) = {f(Symbol('x'))}")
    for x in [-3,-2,0,4]:
        print(f"f({x}) = {f(x)}")
    pass
def opgave2():
    #Opgave 2
    print("===Opgave 2===")
    list_of_pairwise_functions = [
        [lambda x : 2*x+4, lambda x: x+3],
        [lambda x : 2, lambda x: 1/2*x-5],
        [lambda x : x**2+x, lambda x: -x+2]
    ]
    x = Symbol('x')
    for i,function_pair in enumerate(list_of_pairwise_functions):
        f,g = function_pair
        print(f'{i+1}.  f(x) = {f(x)}, g(x) = {g(x)}')
        print(f'    f(g(x)) = {str(f(x)).replace('x','(' + str(g(x)) +')')}   = {expand(f(g(x)))}')
        print(f'    g(f(x)) = {str(g(x)).replace('x','('+str(f(x))+')')}   = {expand(g(f(x)))}\n')
    pass

def opgave3():
    #Opgave 3
    print("===Opgave 3===")
    x = Symbol('x')
    y = Symbol('y')
    list_of_composite_functions = [
        "(x-1)^2",
        "(x-2)^(1/2)",
        "(2x+1)^2-2",
        "sqrt(x^2+2x)"
    ]
    list_of_pairwise_functions = [
        [lambda x : x-1, lambda y: y**2],
        [lambda x : x-2, lambda y: y**(1/2)],
        [lambda x : 2*x+1, lambda y: y**2-2],
        [lambda x : x**2+2*x, lambda y: y**(1/2)]
    ]
    for i,pair in enumerate(list_of_pairwise_functions):
        g,f = pair
        fgx = list_of_composite_functions[i]
        print(f'{i+1}.  f(g(x)) = {fgx}')
        print(f'    g(x) = {g(x)}')
        print(f'    f(y) = {f(y)}\n')
    pass

def opgave4():
    #Opgave 4

    f = lambda x: (2*x-3) * (x <= 4) + (-1/2*x+7)*(x>4)
    print("===Opgave 4===")

    x = np.linspace(0,8,100)
    y = f(x)

    plt.plot(x,y)
    plt.xlabel(r'$x$', fontsize = 14)
    plt.ylabel(r'$y$', fontsize = 14)
    plt.title(r'Parametric Curve')
    plt.axis('equal')
    plt.show()
    pass

def opgave5():
    #Opgave 5
    print("===Opgave 5===")

    f = lambda x: 2*x**3 - 3*x**2 + 4*x -5
    x = np.linspace(-3,3,100)
    y = f(x)
    #plt.plot(x,y)
    #plt.xlabel(r'$x$', fontsize = 14)
    #plt.ylabel(r'$y$', fontsize = 14)
    #plt.title(r'Parametric Curve')
    #plt.axis('equal')
    #plt.show()
    x = Symbol('x',real=True)
    sol1 = solveset(f(x),x, domain = S.Reals)
    print(f"f(x) = 0 <=> x = {sol1.evalf()}")
    print(f"f(0) = {f(0)}")
    print(f'f(-3) = {f(-3)}')
    print(f'f(3) = {f(3)}')
    pass

def opgave6():
    print("===Opgave 6===")
    f = lambda x : x**2+2*x+3
    for x in range(-4,5):
        print(f'f({x}) = {f(x)}')

def opgave7():
    print("====Opgave 7=======")
    f = lambda t : (6 * t) * (t <= 1/4) + (40*(t-1/4)+1.5) * np.logical_and(t > 1/4, t <= 5/4) + (20*(t-5/4)+41.5) * np.logical_and(t > 5/4, t <= 7/4)

    t = np.linspace(0,7/4,100)
    y = f(t)

    plt.plot(t,y)
    plt.xlabel(r'$t$', fontsize = 14)
    plt.ylabel(r'$y$', fontsize = 14)
    plt.yscale('linear')
    plt.title(r'Parametric Curve')
    plt.show()

opgave6()