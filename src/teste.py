def merge_sort(array, key):
    if len(array) > 1:
        meio = len(array) // 2
        esquerda, direita = array[:meio], array[meio:]

        # Chamadas recursivas para as sublistas
        merge_sort(esquerda, key)
        merge_sort(direita, key)

        # Inicializa os índices i, j e k
        i = j = k = 0

        # Combinação das sublistas ordenadas com base na chave
        while i < len(esquerda) and j < len(direita):
            if esquerda[i][key] < direita[j][key]:
                array[k] = esquerda[i]
                i += 1
            else:
                array[k] = direita[j]
                j += 1
            k += 1

        # Verifica se há elementos restantes em ambas as sublistas
        while i < len(esquerda):
            array[k] = esquerda[i]
            i += 1
            k += 1

        while j < len(direita):
            array[k] = direita[j]
            j += 1
            k += 1


# Exemplo de uso
if __name__ == "__main__":
    lista_de_pessoas = [
        {"nome": "Alice", "idade": 28, "cidade": "São Paulo"},
        {"nome": "Bob", "idade": 22, "cidade": "Rio de Janeiro"},
        {"nome": "Charlie", "idade": 35, "cidade": "Belo Horizonte"},
        {"nome": "Diana", "idade": 30, "cidade": "Brasília"}
    ]

    print("Lista de pessoas original:")
    for pessoa in lista_de_pessoas:
        print(pessoa)

    # Ordena a lista de pessoas com base na idade usando Merge Sort
    merge_sort(lista_de_pessoas, key="idade")

    print("\nLista de pessoas ordenada por idade:")
    for pessoa in lista_de_pessoas:
        print(pessoa)
