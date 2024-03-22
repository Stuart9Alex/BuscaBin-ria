def busca_sequencial(lista, chave):
    for i, elemento in enumerate(lista):
        if elemento == chave:
            return i
    return -1

# Exemplo de uso
lista = [1, 4, 3, 5, 2]
chave = 5
print("Posição da chave:", busca_sequencial(lista, chave))
