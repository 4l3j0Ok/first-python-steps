# for x in range(1, 101):
#     print(x)

# for y in range(1, 101, 2): #El tercer parámetro de range indica cuanto se incrementa cada vuelta.
#     print(y)



# #Promedio Notas
# suma = 0
# for f in range(0, 3): #La variable f funciona solo como iterador. Solo sirve para que se repita 10 veces lo que contiene el for.
#     notas = int(input('Ingrese notas: '))
#     suma = suma + notas
# print("La suma de las notas es: ", end="")
# print(suma) 
# promedio = suma / 3
# print('El promedio es: ', end="")
# print(promedio)

#Cantidad de alumnos aprobados

# aprobados = 0
# reprobados = 0

# for f in range(0, 10):
#     nota = float(input('Ingrese notas de los 10 alumnos: '))
#     if nota >= 7:
#         aprobados = aprobados + 1
    
#     else:
#         reprobados = reprobados + 1

# print("La cantidad de aprobados es: ")
# print(aprobados)

# print("La cantidad de reprobados es: ")
# print(reprobados)

#Numeros mayores a 50

# cantidad = 0

# for d in range(0, 5):
#     numero = int(input('Inserte un número: '))

#     if numero >= 50:
#         cantidad = cantidad + 1

#     else:
#         cantidad = cantidad

# print('La cantidad de números ingresados mayor a 50 son: ')    
# print(cantidad)

#Multiplos

mul3 = 0
mul5 = 0

for t in range(1, 10):
    valor = int(input('Ingrese un valor: '))
    if valor%3 == 0: #El signo "%" se usa para calcular el resto de un número entero.
        mul3 = mul3 + 1
    
    if valor%5 == 0:
        mul5 = mul5 + 1

print('La cantidad de valores que son multiplos de 3 son: ')        
print(mul3)

print('La cantidad de valores que son multiplos de 5 son: ')        
print(mul5)