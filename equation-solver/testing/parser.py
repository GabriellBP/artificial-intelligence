from py_expression_eval import Parser
#
# parser = Parser()
#
# operations = ["+", "-", "*", "/"]
#
# eq = "40 * x + 20 = 60"
# eq = eq.split("=")
# print(eq)
# expr = parser.parse(eq[0])
# try:
#     print(int("6.7"))
#     print(float("6.7"))
# except Exception:
#     print("its not a number")
# print(expr.simplify({}).toString())

from math import *
import ast

eq = "pi"
# aste = ast.parse(eq)

print(eval(eq))



