lista = [4, 2, 1, 6, 5, 7, 13, 3, 10, 9, 11, 8, 12]

maior_n = lista[0]

for n in lista:
    if(n > maior_n):
        maior_n = n
print(f"Maior numero na lista: {maior_n}")
