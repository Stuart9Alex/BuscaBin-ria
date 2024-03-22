### Experimentos

```python
import time
import random

def gerar_sequencia(tamanho):
    return [random.randint(0, 1000) for _ in range(tamanho)]

def executar_experimentos(tamanho_sequencia, numero_buscas):
    sequencia = gerar_sequencia(tamanho_sequencia)
    sequencia_ordenada = sorted(sequencia)

    # Medição do tempo para busca sequencial
    inicio = time.time()
    for _ in range(numero_buscas):
        chave = random.choice(sequencia)
        busca_sequencial(sequencia, chave)
    tempo_sequencial = time.time() - inicio

    # Medição do tempo para busca sequencial otimizada
    inicio = time.time()
    for _ in range(numero_buscas):
        chave = random.choice(sequencia_ordenada)
        busca_sequencial_otimizada(sequencia_ordenada, chave)
    tempo_sequencial_otimizada = time.time() - inicio

    # Medição do tempo para busca binária 
    inicio = time.time()
    for _ in range(numero_buscas):
        chave = random.choice(sequencia_ordenada)
        busca_binaria(sequencia_ordenada, chave)
    tempo_binaria = time.time() - inicio

    return tempo_sequencial, tempo_sequencial_otimizada, tempo_binaria

# Execução dos experimentos
tamanho_sequencia = 10000
numero_buscas = 1000
tempo_sequencial, tempo_sequencial_otimizada, tempo_binaria = executar_experimentos(tamanho_sequencia, numero_buscas)

print("Tempo médio para busca sequencial:", tempo_sequencial)
print("Tempo médio para busca sequencial otimizada:", tempo_sequencial_otimizada)
print("Tempo médio para busca binária:", tempo_binaria)
