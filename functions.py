#Las funciones que vienen instaladas en python pueden ser dir, type, print, etc.
#Lo que permitirá la palabra clave "def" es que se pueda crear una  nueva función.
#En esta primer función creamos el "holaMundo", cada vez que se le llame imprimirá el mensaje "Hola Mundo"
#Esto de las funciones sirve para encapsular código que se puede reutilizar, con lo cual el cçodigo ocupa menos.
def holaMundo():
    print("Hola Mundo")

#En esta segunda creamos el "hola", cada vez que se le llame mostrará el mensaje "Hola"
#mas el nombre y apellido que se le haya pedido al usuario.
#Lo que se haca acá es que se le asignan parámetros a la función, en este caso, "nombre" y "apellido".
def hola(nombre, apellido):
    print("Hola", nombre, apellido)

holaMundo()
hola(input('Inserte su nombre: '), input('Inserte su apellido: '))
#Acá se le pide al usuario que le asigne un valor a los parámetros.

def suma (n1, n2):
    r = n1 + n2
    print("El resultado de la suma es:", r)

suma(int(input("Inserte un número a sumar: ")), int(input("Inserte otro número a sumar: ")))

#Otra forma de hacer lo mismo

def suma2 (n1, n2):
    return("El resultado es: ", n1 + n2)

print(suma2(int(input("Inserte un número a sumar: ")), int(input("Inserte otro número a sumar: "))))

#Lambda

suma3 = lambda n1, n2: n1 + n2

print(suma3(int(input('Inserte un número a sumar: ')), (int(input('inserte otro número a sumar:')))))