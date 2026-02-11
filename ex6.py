def retorna_quadrado(graos):
    for i in range(0, (graos // 2) + 1):
        if((2**i) == graos):
            return i + 1
    



user_input = int(input("Digite o número de grãos: "))
print(f"Quadrado: {retorna_quadrado(user_input)}")
