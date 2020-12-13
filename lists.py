#Formas de crear una lista

lista1 = [1, 'HOLA', 'Violeta', 2.5, 'jaja xd', True, [1, 2, 3]] #Se pueden almacenar cualquier tipo de dato dentro de la lista.
print(lista1)

listaColores = list(("Azul", "Violeta", "Negro"))
listaaa = list(listaColores)
print(type(listaaa))

print(type(listaColores))
print(listaColores)

# #Insertar un elemento a la lista

lista2 = [int(input("inserte números: "))] 
print(type(lista2))
print(lista2)

#Lista a partir de rangos

listaRango = list(range(1, 11)) #Imprime del 1 al 10 solamente porque sí, por lo cual se debe sumar un numero más al que quieres que imprima.
print(listaRango)

#Propiedades de Listas (dir)

print(dir(listaColores)) #Funciona para saber qué propiedades podemos aplicar a la lista
print(len(listaColores)) #Mostraría cuantos elementos hay en una lista 
print(listaColores[2]) #Mostraría el segundo elemento de la lista.
print('Azul' in listaColores) #Buscar si determinado texto está en una lista.

#Cambiar elementos de la lista

print(listaColores)
listaColores [2] = 'Gris'
print(listaColores)

print(lista1)
lista1 [0] = 23
print(lista1)

#Agregar o quitar elementos a la lista
print(listaColores)

listaColores.append('Rosa') #1 solo elemento
print(listaColores)

listaColores.extend(('Amarillo', 'Púrpura')) #2 o más elementos. Se debe usar una Tupla (doble paréntesis)
print(listaColores)

listaColores.insert(2, 'Marrón') #"insert" sirve para agregar elementos en determinada posición de la lista.
print(listaColores)

listaColores.pop() #Elimina el último elemento de la lista.
print(listaColores)

listaColores.pop(1) #Elimina el elemento de índice definido.
print(listaColores)

listaColores.remove('Rosa') #Elimina un item en concreto.
print(listaColores)

listaColores.clear() #Elimina todos los items de la lista.
print(listaColores)

#Ordenar elementos de la lista

listaColores.sort() #Ordena los elementos alfabéticamente.
print(listaColores)

listaColores.sort(reverse=True) #Ordena los elementos a la Z a la A (reverso).
print(listaColores)

print(listaColores.index('Azul')) #Revela la posición de un item en concreto.
print(listaColores)
print(listaColores.count('Amarillo')) #Cuenta las veces que está un item en concreto dentro de la lista.