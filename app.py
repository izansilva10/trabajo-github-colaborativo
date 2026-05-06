def calcular(lista):
    total = 0
    for num in lista:
        total = total + num
    return total

numeros = [10, 20, 30, 40, 50]
resultado = calcular(numeros)
print("Resultado: " + str(resultado))
