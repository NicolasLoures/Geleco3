def sum(lista):
    total = 0
    for item in lista:
        if isinstance(item, list):
            total += sum(item)
        else:
            total += item
    return total

print(sum([1, 4, [5, -3.0, [-10, 5]], 9])) 