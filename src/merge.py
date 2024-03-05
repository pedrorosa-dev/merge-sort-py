def merge_sort(array):
    if len(array) > 1:
        meio = len(array) // 2
        esquerda, direita = array[:meio], array[meio:]
        merge_sort(esquerda)
        merge_sort(direita)
        array[:] = sorted(esquerda + direita)
