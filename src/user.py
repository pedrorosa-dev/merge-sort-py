from src.merge import merge_sort


def main():
    numeros = []

    while True:
        try:
            num = input("Digite um número (ou 's' para parar): ")
            if num.lower() == 's':
                break
            numeros.append(int(num))
        except ValueError:
            print("Por favor, digite um número válido.")

    if numeros:
        print("Lista original:", numeros)
        merge_sort(numeros)
        print("Lista ordenada merge sort:", numeros)
    else:
        print("A lista está vazia.")
