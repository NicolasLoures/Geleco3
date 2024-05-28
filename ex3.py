def soma(A, B):
  C = {"n": A["n"]}

  for key in A:
      if key != "n":
          C[key] = A[key]

  for key in B:
      if key != "n":
          if key in C:
              C[key] += B[key]
          else:
              C[key] = B[key]

  return C

print(soma({"n": 2, (0, 0): 1}, {"n": 2, (1, 0): 5}))  
print(soma({"n": 2, (1, 0): 1}, {"n": 2, (1, 0): 5}))  
