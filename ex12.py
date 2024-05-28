def ehjson(dic):
  return all(isinstance(key, str) for key in dic.keys())

print(ehjson({"Nome": "Andre", "Idade": 33}))  #
print(ehjson({1: 2, 3: 4})) 
