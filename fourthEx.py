from sympy import Matrix, linsolve, symbols

def fourthEx():
  x, y, z = symbols("x, y, z")
  A = Matrix([[1, -4, 2], [0, -5, -10]])
  b = Matrix([0,0])
  output = linsolve((A, b), [x, y, z])
  print(output)