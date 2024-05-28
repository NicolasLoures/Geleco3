def soma(x, y):
  try:
      resultado = float(x) + float(y)
      return resultado
  except ValueError:
      return None

print(soma(2, 'a'))  
