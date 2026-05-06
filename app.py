def calcular(lista):
    total = 0
    for num in lista:
        total = total + num
    return total

numeros = [1, 2, 3, 4, 5]
resultado = calcular(numeros)
print("Resultado: " + str(resultado))
