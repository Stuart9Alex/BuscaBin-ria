#******************************************************************************

#Welcome to GDB Online.
#GDB online is an online compiler and debugger tool for C, C++, Python, PHP, Ruby, 
#C#, OCaml, VB, Perl, Swift, Prolog, Javascript, Pascal, COBOL, HTML, CSS, JS
#Code, Compile, Run and Debug online from anywhere in world.

#*******************************************************************************/
import time
import random

def busca_sequencial(chave, sequencia):
    for i in range(len(sequencia)):
        if sequencia[i] == chave:
            return i
    return -1

def analise_empirica(n, q):
    sequencia = [random.randint(1, n) for _ in range(n)]
    chaves = [random.randint(1, n) for _ in range(q)]
    
    tempos = []
    
    for chave in chaves:
        inicio = time.time()
        busca_sequencial(chave, sequencia)
        fim = time.time()
        tempo_total = fim - inicio
        tempos.append(tempo_total)
    
    tempo_medio = sum(tempos) / len(tempos)
    return tempo_medio

if __name__ == "__main__":
    ns = [10**4, 10**5, 10**6, 10**7]
    q = 1000
    
    for n in ns:
        tempo_medio = analise_empirica(n, q)
        print(f"Para n={n}, tempo médio de busca sequencial: {tempo_medio:.6f} segundos")
