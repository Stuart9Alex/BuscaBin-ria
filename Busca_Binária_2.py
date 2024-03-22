### Busca Binária 2

```python
def busca_binaria(lista, chave):
    inicio = 0
    fim = len(lista) - 1
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio] == chave:
            return meio
        elif lista[meio] < chave:
            inicio = meio + 1
        else:
            fim = meio - 1
    return -1
