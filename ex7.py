def muda(texto, indice, c):
  tamanho = len(texto)
  novo_texto = texto[:indice] + c + texto[indice + 1:] if indice < tamanho else texto + c
  return novo_texto

print(muda('Testes', 5, 'X'))   
print(muda('Testes', 4, 'X'))   
print(muda('Testes', 100, 'X')) 
