def merge_sort(array):
    if len(array) > 1:
        ListaDoMeio = len(array) // 2
        ListaDaEsquerda, ListaDaDireita = array[:ListaDoMeio], array[ListaDoMeio:]
        merge_sort(ListaDaEsquerda)
        merge_sort(ListaDaDireita)
        array[:] = sorted(ListaDaEsquerda + ListaDaDireita)
