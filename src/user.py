from src.merge import merge_sort


def main():
    numbers = []

    while True:
        try:
            num = input("Digite um número (ou 's' para parar): ")
            if num.lower() == 's':
                break
            numbers.append(int(num))
        except ValueError:
            print("Por favor, digite um número válido.")

    if numbers:
        print("Lista original:", numbers)
        merge_sort(numbers)
        print("Lista ordenada:", numbers)
    else:
        print("A lista está vazia.")
