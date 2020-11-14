from py_expression_eval import Parser
parser = Parser()

valor = parser.parse('2 * 3').evaluate({})
print(valor)


from asteval import Interpreter
aeval = Interpreter()
txt = """nmax = 1e8
a = sqrt(arange(nmax))
"""
valor = aeval.eval(txt)
print(valor)
