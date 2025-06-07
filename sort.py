#Código feito por: Guilherme Gabril
#Data: 02/06/2025
#Algoritimos de Ordenação: Quick-Sort e Insertion-Sort, para ordenação de vetores com números: crescentes, decrescentes e aleatórios. Vetores de tamanho: 50, 500, 5000 e 50000.
#Gráficos para análise do tempo de cada algoritimo mediante a um vetor inicial em ordem crescente, decrescente ou aleatório.

#Bibliotecas
import random
import time
import matplotlib.pyplot as plt

# Quick-Sort 
def quicksort(vetor):
    n = len(vetor)
    # Base para recursão
    if n <= 1:
        return vetor
    
    #Escolhe um pivo aleatorio
    index_pivo = random.randint(0, n - 1)
    vetor[index_pivo], vetor[n - 1] = vetor[n - 1], vetor[index_pivo]
    
    # Define o pivo
    pivo = vetor[n - 1]
    k = -1

    # Organizando os valores maiores e menores que o pivo
    for i in range(0, n):
        if vetor[i] < pivo:
            k = k + 1
            aux = vetor[i]
            aux_2 = vetor[k]

            vetor[k] = aux
            vetor[i] = aux_2

    # coloca o pivo na posição correta
    vetor[k + 1], vetor[n - 1] = vetor[n - 1], vetor[k + 1]

    vetor_1 = vetor[0:k + 1]  # valores menores que o pivo
    vetor_2 = vetor[k + 2:n]  # valores maiores que o pivo

    ordenap1 = quicksort(vetor_1)  # ordena os valores menores
    ordenap2 = quicksort(vetor_2)  # ordena os valores maiores

    return ordenap1 + [pivo] + ordenap2 # Junta tudo

#Insertion-Sort
def insertionsort(vetor):
    n = len(vetor)
    for i in range(0, n):
        #variável para ao realizar a troca  e  analisar também os outros valores anteriores a troca
        j = i
        while j > 0 and vetor[j - 1] > vetor[j]: #verifica se o valor anterior é maior que o atual
            #variáveis auxiliares para não perder os valores
            aux_1 = vetor[j-1]
            aux_2 = vetor[j]

            #realização da troca de posição 
            vetor[j] = aux_1
            vetor[j-1] = aux_2

            #altera o valor para analisar os termos anteriores também
            j = j - 1
    return vetor

#Função que gera os vetores para ordenação
def gerar_vetores(tamanho):
    crescente = list(range(1, tamanho + 1))
    decrescente = list(range(tamanho, 0, -1))
    aleatorio = [random.randint(0, 99999) for _ in range(tamanho)]

    return crescente, decrescente, aleatorio

#Função que verifica o tempo para o Quick-sort
def timer_quick(vetor):
    vetor_copy = list(vetor)
    inicio = time.time()
    quicksort(vetor_copy)
    fim = time.time()
    return fim - inicio

#Função que verifica o tempo para Insertion-sort
def timer_insert(vetor):
    vetor_copy = list(vetor)
    inicio = time.time()
    insertionsort(vetor_copy)
    fim = time.time()
    return fim - inicio

# Tamanho dos vetores
tamanhos = [50, 500, 5000, 50000]

# Listas para salvar os tempos 
tempos_quick_crescente = []
tempos_insert_crescente = []

tempos_quick_decrescente = []
tempos_insert_decrescente = []

tempos_quick_aleatorio = []
tempos_insert_aleatorio = []

#Executa a ordenação e calcula o tempo para os vetores de tamanho 50, 500, 5000 e 50000
for tamanho in tamanhos:
    print(f"\nTestando com vetor de tamanho {tamanho}")
    crescente, decrescente, aleatorio = gerar_vetores(tamanho)


    t_quick_c = timer_quick(crescente)
    t_insert_c = timer_insert(crescente)
    tempos_quick_crescente.append(t_quick_c)
    tempos_insert_crescente.append(t_insert_c)

    print(f"  Crescente:")
    print(f"    QuickSort:     {t_quick_c:.5f} segundos")
    print(f"    InsertionSort: {t_insert_c:.5f} segundos")

    t_quick_d = timer_quick(decrescente)
    t_insert_d = timer_insert(decrescente)
    tempos_quick_decrescente.append(t_quick_d)
    tempos_insert_decrescente.append(t_insert_d)

    print(f"  Decrescente:")
    print(f"    QuickSort:     {t_quick_d:.5f} segundos")
    print(f"    InsertionSort: {t_insert_d:.5f} segundos")

  
    t_quick_a = timer_quick(aleatorio)
    t_insert_a = timer_insert(aleatorio)
    tempos_quick_aleatorio.append(t_quick_a)
    tempos_insert_aleatorio.append(t_insert_a)

    print(f"  Aleatório:")
    print(f"    QuickSort:     {t_quick_a:.5f} segundos")
    print(f"    InsertionSort: {t_insert_a:.5f} segundos")


# Gráfico para o vetor Crescente
plt.figure(figsize=(10, 6))
plt.plot(tamanhos, tempos_quick_crescente, marker='o', label='QuickSort', color='blue')
plt.plot(tamanhos, tempos_insert_crescente, marker='o', label='InsertionSort', color='red')
plt.title('Tempo de Execução x Tamanho do Vetor (Crescente)')
plt.xlabel('Tamanho do Vetor')
plt.ylabel('Tempo (segundos)')
plt.xscale('log')  
plt.xticks(tamanhos, labels=tamanhos)  
plt.legend()
plt.grid(True, which="both", linestyle='--')
plt.tight_layout()
plt.show()


# Gráfico para vetor Decrescente
plt.figure(figsize=(10, 6))
plt.plot(tamanhos, tempos_quick_decrescente, marker='o', label='QuickSort', color='blue')
plt.plot(tamanhos, tempos_insert_decrescente, marker='o', label='InsertionSort', color='red')
plt.title('Tempo de Execução x Tamanho do Vetor (Decrescente)')
plt.xlabel('Tamanho do Vetor')
plt.ylabel('Tempo (segundos)')
plt.xscale('log')
plt.xticks(tamanhos, labels=tamanhos)
plt.legend()
plt.grid(True, which="both", linestyle='--')
plt.tight_layout()
plt.show()


# Gráfico para vetor Aleatório
plt.figure(figsize=(10, 6))
plt.plot(tamanhos, tempos_quick_aleatorio, marker='o', label='QuickSort', color='blue')
plt.plot(tamanhos, tempos_insert_aleatorio, marker='o', label='InsertionSort', color='red')
plt.title('Tempo de Execução x Tamanho do Vetor (Aleatório)')
plt.xlabel('Tamanho do Vetor')
plt.ylabel('Tempo (segundos)')
plt.xscale('log')
plt.xticks(tamanhos, labels=tamanhos)
plt.legend()
plt.grid(True, which="both", linestyle='--')
plt.tight_layout()
plt.show()