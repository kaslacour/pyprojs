from sympy.parsing.sympy_parser import parse_expr
from sympy import expand, Subs

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

#Opgave 1
list_of_expressions_1 = [
    "2*(7+3)",
    "2*7+3",
    "2*7+2*3",
    "15/5+4",
    "5-30/5",
    "(30-15)/3",
    "(18-12)/3",
    "3*8+4/2",
    "6+8/2-1"
]
print("===Opgave 1====")
for idx, expr in enumerate(list_of_expressions_1):
    print(str(idx+1)+".",end=" ")
    print_exercise_with_solution(expr)

#Opgave 2
list_of_expressions_2 = [
    "-2**3",
    "(-2)**3",
    "-5**2",
    "(-5)**2",
    "(3*4)**2",
    "3*4**2",
    "(2a)**2",
    "2a*a",
    "(4a)**3"
]
print("===Opgave 2===")
for idx,expr in enumerate(list_of_expressions_2):
    print(str(idx+1)+".",end=" ")
    print_exercise_with_solution(expr)

from sympy import Symbol
a,b,c,d = Symbol('a'), Symbol('b'),Symbol('c'),Symbol('d')
x,y = Symbol('x'), Symbol('y')

#Opgave 3
list_of_expressions_3 = [
    "-3*(x-y)", 
    "x*(2-y)",
    "(3-x)*2",
    "2*(6-y)",
    "3*a*(6-a)",
    "3*(2-a)*2"
]
print("===Opgave 3===")
for idx,expr in enumerate(list_of_expressions_3):
    print(str(idx+1)+".",end=" ")
    print_exercise_with_solution(expr)

#Opgave 4
list_of_expressions_4 = [
    "ab-c",
    "a(b-c)",
    "ab-cd",
    "ab+cd",
    "a-b(c+d)",
    "(a-b)*(c+d)",
    "(a-b)*c+d"
]
print("===Opgave 4===")
print("a = 2", "b = -3", "c = 4", "d = -5")
for idx,expr in enumerate(list_of_expressions_4):
    print(str(idx+1)+".",end=" ")
    print_exercise_with_solution(expr,vars=[a,b,c,d],values=[2,-3,4,-5])

#Opgave 5
list_of_expressions_5 = [
    "5(p-2q-r)+3(p-q+2r)",
    "2(a+2b)+(a-b)",
    "4(c-d)-3(c+2d)",
    "4(a+5b)+7(3a+b)",
    "3(7a+b)+8(a+3b)",
    "a(a-b)+b(a+b)"
]
print("===Opgave 5===")
for idx,expr in enumerate(list_of_expressions_5):
    print(str(idx+1)+".",end=" ")
    print_exercise_with_solution(expr)

print("===Opgave 6===")
expr = "43**2"
tekst = """I året {0} = {1} var matematikeren Augustus de Morgan {2} år gammel. 
Altså var han født i år {3} = {4} efter kristus fødsel.""".format(expr.replace("**","^"),eval(expr), 43, str(eval(expr)) + " - 43",eval(expr)-43)
print(tekst)
