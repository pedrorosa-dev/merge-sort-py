## Documentação do Projeto

## Estrutura do Projeto

O projeto está organizado na seguinte estrutura de diretórios:

```bash
merge-sort-py/
|-- docs/
|  |-- docs.md
|-- src/
|   |-- merge.py
|   |-- user.py
|-- main.py
|-- readme.md
```

1. docs: pasta contendo a documentacao do codigo

2. src: Pasta contendo os módulos Python.
3. merge.py: Módulo contendo a implementação da função merge_sort.
4. user.py: Módulo principal onde o código do usuário é definido.

5. main.py: Arquivo principal que inicia o programa.

6. readme.md: Introducao ao projeto.

## Explicação do codigo

1. merge.py

O módulo merge.py contém a implementação do algoritmo de ordenação merge_sort. A função merge_sort utiliza o método de ordenação por fusão para ordenar uma lista.

2. user.py

No módulo user.py, a função merge_sort do módulo merge é importada. Este módulo contém a lógica do usuário para interagir com o programa.

3. main.py

O arquivo main.py importa as funções e classes do módulo user e inicia o programa chamando a função main do módulo user.

## Uso do Programa

O usuário é solicitado a inserir números continuamente. Para encerrar a entrada de números, o usuário pode digitar 's'. Apos encerrar o programa, ira mostrar a lista original e a lista com o merge sort.

## Execução do Programa

Execute o programa a partir do diretório principal e no arquivo main.py usando o seguinte comando no terminal :

```bash
python3  main.py
```
