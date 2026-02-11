primeira_mao = [13, 2, 1, 6, 5, 7, 4, 3, 10, 9, 11, 8, 12]
segunda_mao = primeira_mao[0]
done = False


def ordenar(lista, inicio, fim):
    meio = 0
    if(inicio >= fim): return
    meio = dividir(lista, inicio, fim)
    ordenar(lista, inicio, (meio - 1))
    ordenar(lista, meio + 1, fim)



def dividir(lista, inicio, fim):
    elemento_parcial = lista[inicio]

    while(True):
        while(inicio < fim and elemento_parcial <= lista[fim]):
            fim -= 1
        if(inicio >= fim): break
        lista[inicio] = lista[fim]
        inicio += 1

        while(inicio < fim and lista[inicio] <= elemento_parcial):
            inicio += 1
        if(inicio >= fim): break
        lista[fim] = lista[inicio]
        fim -= 1

    lista[fim] = elemento_parcial
    return fim

ordenar(primeira_mao, 0, len(primeira_mao) - 1)
print(primeira_mao)
