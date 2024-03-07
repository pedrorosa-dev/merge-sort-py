from src.merge import merge_sort


def main():
    ListaDosNumeros = []
    while True:
        try:
            num = input("Digite um número (ou 's' para parar): ")
            if num.lower() == 's':
                break
            ListaDosNumeros.append(int(num))
        except ValueError:
            print("Por favor, digite um número válido.")

    if ListaDosNumeros:
        print("Lista nao ordenada com merge sort:", ListaDosNumeros)
        merge_sort(ListaDosNumeros)
        print("Lista ordenada merge sort:", ListaDosNumeros)
    else:
        print("A lista está vazia.")
