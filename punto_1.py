def triangulo_numerico(n):
    for i in range(1, n+1):

        print("")

        for n in range(1, i+1):
            print(i, end="")

triangulo_numerico(int(input('Inserte un número: ')))

