def soma(A, B):
  resultado = [[0 for _ in range(len(A[0]))] for _ in range(len(A))]

  for i in range(len(A)):
      for j in range(len(A[0])):
          resultado[i][j] = A[i][j] + B[i][j]

  return resultado

A = [[1, 2], [3, 4]]
B = [[3, 1], [-1, -3]]
resultado = soma(A, B)
print(resultado)  
