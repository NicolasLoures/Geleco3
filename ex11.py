def meudict_auxiliar(lista, d):
  if not lista:
      return d
  name, age = lista[0]
  if name not in d:
      d[name] = age
  return meudict_auxiliar(lista[1:], d)

def meudict(lista):
  return meudict_auxiliar(lista, {})

print(meudict([('Andre', 33), ('Lucas', 30), ('Andre', 32), ('Clara', 28), ('Clara', 50)]))
