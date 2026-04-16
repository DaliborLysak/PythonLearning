from sympy import symbols, diff, Eq, init_printing, Function
from IPython.display import display

init_printing(use_latex=True)

x = symbols('x')
f =  Function('f')(x)
f_expr = x**3 + 2*x**2 + 5*x + 7
df = diff(f_expr, x)

display(Eq(f, f_expr))
display(Eq(diff(f, x), df))