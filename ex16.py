def menor(lista):
  menor_elemento = min(lista)
  posicoes = [i for i, x in enumerate(lista) if x == menor_elemento]
  return (menor_elemento, posicoes)

print(menor([1, 2, 3]))  
print(menor([1, 2, 1]))  
