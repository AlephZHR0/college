from random import randint

def heap_sort(vetor:list, tamanho:int):
    cria_heap(vetor, tamanho)
    fim = tamanho - 1
    while fim > 0:
        swap(vetor, 0, fim)
        fim -= 1
        arruma_heap(vetor, 0, fim)

def cria_heap(vetor:list, tamanho:int):
    inicio = int((tamanho - 1) / 2)
    while inicio >= 0:
        arruma_heap(vetor, inicio, tamanho - 1)
        inicio -= 1

def arruma_heap(vetor:list, inicio:int, fim:int):
    raiz = inicio
    while raiz * 2 + 1 <= fim:
        filho = raiz * 2 + 1
        trocar = raiz
        if vetor[trocar] < vetor[filho]:
            trocar = filho
        if filho + 1 <= fim and vetor[trocar] < vetor[filho + 1]:
            trocar = filho + 1
        if trocar == raiz:
            return
        else:
            swap(vetor, raiz, trocar)
            raiz = trocar

def swap(vetor:list, i:int, j:int):
    vetor[i], vetor[j] = vetor[j], vetor[i]

def main(vetor:list):
    heap_sort(vetor, len(vetor))
    print(vetor)

if __name__ == '__main__':
    tamanho_vetor = 15
    vetor = [randint(0, 100) for _ in range(tamanho_vetor)]
    print(vetor)
    main(vetor)