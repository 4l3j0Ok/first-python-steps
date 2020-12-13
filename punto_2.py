def anagramas_unicos(lista):

    item1 = lista[0]
    item2 = lista[1]
    item3 = lista[2]
    
    item1sort = sorted(item1)
    item2sort = sorted(item2)
    item3sort = sorted(item3)

    if item1sort == item2sort:
        nuevalista = [item1, item3]
        print(nuevalista)
        
    elif item1sort == item3sort or item2sort == item3sort:
        nuevalista2 = [item1, item2]
        print(nuevalista2)
        
    else:
        print(lista)

anagramas_unicos(["isla", "pan", "lisa"])

