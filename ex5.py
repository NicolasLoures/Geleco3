def retira(lista, n):
    lista_sem_repeticao = list(set(lista))
    while n in lista_sem_repeticao:
        lista_sem_repeticao.remove(n)
    lista_sem_repeticao.sort()
    return lista_sem_repeticao

print(retira([5, 1, 8, 4, 3, 5], 8))  