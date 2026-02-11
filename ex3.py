lista = [2, 4, 6, 8, 10, 12, 13]
passos = 0

for n in lista:
    if n == 8:
        passos += 1
        break
    passos += 1

print(f"Passos: {passos}")
