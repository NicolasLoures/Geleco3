def palindromo(palavra):
  return palavra == palavra[::-1]

print(palindromo('osso'))   
print(palindromo('ossos'))  