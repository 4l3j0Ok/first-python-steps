#La principal diferencia de los sets con las lists es que estos últimos no tienen un órden por índice ({1}, {2}, etc).

colores = {'Rojo', 'Verde', 'Azul'} #Formato de sets.

print(colores)
print(type(colores)) #Para saber qué tipo de dato es la variable.
print('Rojo' in colores) #Para saber si determinado elemento está dentro del set (devuelve un booleano).

colores.add('Amarillo') #Agregar elemento al set.
print(colores)

colores.remove('Verde') #Eliminar elemento del set.
print(colores)

colores.clear() #limpiear el set.
print(colores)

#del colores #Elimina el set.
#print(colores)