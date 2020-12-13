myStr = "Hello World"
#dir sirve para obtener propiedades y/o métodos de una variable
#print(dir(myStr))

#Algunas propiedades obtenidas mediante el dir:
#esto puede servir para no modificar el valor de la variable.

print(myStr.upper()) #upper es un método que convierte todo el texto en mayúsculas.
print(myStr.lower()) #lower hace lo mismo pero con minúsculas.
print(myStr.swapcase()) #invierte las minúsculas y mayúsculas.
print(myStr.capitalize()) #Deja en mayúsculas el primer caracter.
print(myStr.replace("Hello", "Bye").upper) #replace reemplaza una parte del texto por otra. Además se pueden encadenar varios métodos.

#Algunas otras útiles

print(myStr.count("l")) #Cuenta cuantas veces se utiliza el caracter. en este caso "l".
print(myStr.startswith("Hello")) #startswith indica si una variable empieza con alguna palabra o con una letra en específico.
print(myStr.startswith("Bye")) #Utiliza los booleanos, por lo cual responde por true o por false.
print(myStr.endswith("World")) #Lo mismo pero si termina.
print(myStr.split()) #Separa las líneas de texto basado en un caracter vacío.
print(myStr.split("e")) #Se puede indicar por donde separar a la hora de mostrar.
print(myStr.isnumeric()) #Indica si el valor de la variable es numérico.
print(myStr.isalpha()) #Indica si el valor de la variable es alfanumérico.
#Índice

print(myStr.find("Hello")) #indica en qué lugar está una palabra o letra comenzando desde el 0.
print(len(myStr)) #indica cuantos caracteres contiene la variable comenzando en el 0.
print(myStr.index("o")) #lo mismo que find.
print(myStr[0]) #De esta manera se le indica al programa que imprima determinado caracter basándose en la posición de éste.
print(myStr[1])
print(myStr[2])
print(myStr[3])
print(myStr[4])
print(myStr[-5])
print(myStr[-4])
print(myStr[-3])
print(myStr[-2])
print(myStr[-1]) #se puede indicar también de manera inversa.


#Concadenación de strings.

print("El nombre del programa es: " + myStr)
print(f"El nombre del programa es: {myStr}") #"f" es la clave para indicar que lo que esté entre corchetes será una variable sin necesidad del "+".
print("El nombre del programa es: {0}".format(myStr))
print("El nombre del programa es: {0} {1}".format(myStr, ", el mejor programa del mundo.")) #Como en C# se puede imprimir con corchetes con 0, 1, 2 etc.
