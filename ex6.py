def retira(texto, c):
  resultado = ''.join([char for char in texto if char != c])
  print(resultado)

retira('Testes', 'e') 
