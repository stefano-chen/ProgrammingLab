def sum_list(lista):
    if len(lista) == 0:
        return None
    result = 0
    for item in lista:
        result += item
    return result
