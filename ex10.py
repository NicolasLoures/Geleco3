def mediana(idades):
    idades_lista = list(idades.values())
    idades_ordenadas = sorted(idades_lista)
    meio = len(idades_ordenadas) // 2
    return (idades_ordenadas[meio] if len(idades_ordenadas) % 2 != 0 
            else (idades_ordenadas[meio - 1] + idades_ordenadas[meio]) / 2)

print(mediana({"Andre": 33, "Lucas": 30, "Clara": 28}))  
