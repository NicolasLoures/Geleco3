def ehpar(n):
  if isinstance(n, int):
      return n % 2 == 0
  else:
      return None

print(ehpar(2))  
print(ehpar(3))  
