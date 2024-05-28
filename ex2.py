def transposta(M):
  return [[M[j][i] for j in range(len(M))] for i in range(len(M[0]))]


M = [[1, 2], [3, 4]]
Mt = transposta(M)
print(Mt)  
