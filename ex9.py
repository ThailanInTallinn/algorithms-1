done = False
lista = [9, 8, 7, 6, 5, 4, 3, 2, 1]
print(f"Lista inicial: {lista}")

while(not done):
    done = True
    for i in range(0, len(lista) - 1):
        if(lista[i] > lista[ i + 1 ]):
            temp = lista[ i + 1 ]
            lista[ i + 1 ] = lista[i]
            lista[i] = temp
            done = False

print(f"Lista final: {lista}")
