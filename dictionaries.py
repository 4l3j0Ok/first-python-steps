#Los diccionarios se emplean cuando hay una clave y un valor. Es como una mini base de datos.

carritoCompras = {
    'Producto': 'libro',
    'Precio': 300,
    'Descripción': 'Mejor libro del mundo',
    'Cantidad': 1,
    'prueba': [{
        'asdasd': 2,
        'dddd': 3
        },
        {
        'asdasd': 8,
        'dddd': 7
        },
        {
        'asdasd': 4,
        'dddd': 6
        }
    ]
}
#Se debe agregar una clave y un valor, separados por ":"

print(carritoCompras)
print(type(carritoCompras))

print(carritoCompras.keys()) #Muestra solo las claves
print(carritoCompras.items()) #Muestra todo el diccionario separado por tuplas.

#Diccionarios dentro de lista.
persona = [
    {
        'Nombre': 'Alejo',
        'Apellido': 'Sarmiento',
        'DNI': 42887583,
        'Fecha nacimiento': '02-02-2001'
    },

    {
        'Nombre': 'Demetrio',
        'Apellido': 'Dowbnac',
        'DNI': 42887495,
        'Fecha nacimiento': '24-09-2000'
    },

    {
        'Nombre': 'Micol',
        'Apellido': 'O´Lery',
        'DNI': 42548644,
        'Fecha nacimiento': '04-12-2000'
    }
]

print(type(persona))