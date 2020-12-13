x = int(input('Inserte un valor para X: '))

if x < 30:

    print('X es menor que 30.')

#elif se utiliza como otro if del mismo condicional, con esto se puede ir directo al else sin necesidad de crear otro if.
elif x == 30:
    
    print('X es 30.')

else:

    print('X es mayor que 30.')

console.log(x)
###################################################################

color = (input('Inserte un color: '))

if color == 'Azul':
    print('El color es Azul.')
else:
    print('El color no es Azul.')


#Condicionales anidadas (If dentro de If).

nombre = input('Inserte su nombre: ')
apellido = input('Inserte su apellido: ')

if nombre == 'Alejo':
    if apellido == 'Sarmiento':
        print('Vos sos Alejo el mejor del universo.')
    else:
        print('Vos sos otro Alejo.')

else:
    print('Vos no sos Alejo el Dios.')

#Operadores lógicos.

numero = int(input('Inserte un número: '))
numero2 = 45
if numero >= 1 and numero <= 10:
    print("El número está entre el 1 y el 10.")

else:
    print("El número no está entre el 1 y el 10.")

if numero >= 1 or numero <=20:
    print("El número es mayor que 1 o menor que 20.")

else:
    print("El número no es mayor que 1 o no es menor que 20.")

if (not(numero == numero2)):
    print("El número no es igual a 45.")
else:
    print("El número es 45.")