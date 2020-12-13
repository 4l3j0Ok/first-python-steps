def calculo(numA, numB, signo):

    if signo == '+':
        rSuma = numA + numB
        print("El resultado de la suma es:", rSuma)

    elif signo == '-':
        rRest = numA - numB
        print("El resultado de la resta es:", rRest)

    elif signo == '/':
        rDiv = numA / numB
        print("El resultado de la división es:", rDiv)  
    
    elif signo == '*':
        rMult = numA * numB
        print("El resultado de la multiplicación es:", rMult)

    else:
        print("Error: Entrada no válida.")

calculo(int(input("Inserte un número: ")),int(input("Inserte otro número: ")), input("¿Qué desea hacer con ellos? (insertar signo: +, -, /, *): "))
