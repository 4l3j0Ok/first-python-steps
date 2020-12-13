frutas = ['Manzana', 'Naranja', 'Mandarina']

#para no tener que imprimir elementos por separado a medida que se agregan,
#se usa for para no tener que escribir la operación. Este for mostrará individualmente cada elemento de la lista.
print(frutas)

frutas.append(input('Inserte otra fruta: '))

for fruta in frutas:
    print(fruta)

#break funciona para romper con el bucle, lo cual hace que pare de ejecutar la operación de bucle.
#continue funciona para omitir determinado elemento de la lista. Ejemplo: if nuevafruta == banana: continue.

for numero in range(1, 9): #Acá ocurrira que imprimirá los números de este rango individualmente.
    print(numero) 

for letras in 'ABCDEFG': #Acá ocurrira que imprimirá las letras de este string de manera individual.
    print(letras)

#Bucle while

contador = 1

#El while funciona como bucle condicional, es decir, sería un "siempre y cuando se cumpla esto, haz esto."
while contador <=10: 
    print(contador)
    contador = contador + 1