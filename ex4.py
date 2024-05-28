def ordena_par(A):
  def num_pares_e_linha(linha):
      num_pares = sum(1 for x in linha if x % 2 == 0)
      return (num_pares, linha)

  return sorted(A, key=num_pares_e_linha)

matriz = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]

print(ordena_par(matriz))

