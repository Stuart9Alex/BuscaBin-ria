### Busca Sequencial Otimizada

def busca_sequencial_otimizada(lista, chave):
    for i, elemento in enumerate(lista):
        if elemento == chave:
            return i
        elif elemento > chave:
            return -1
    return -1

# Exemplo de uso
lista_ordenada = [1, 2, 3, 4, 5]
chave = 5
print("Posição da chave:", busca_sequencial_otimizada(lista_ordenada, chave))

