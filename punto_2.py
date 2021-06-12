def anagramas_unicos(lista):
    if sorted(lista[0]) == sorted(lista[1]):
        nuevalista = [lista[0], lista[2]]
        print(nuevalista)

    elif sorted(lista[0]) == sorted(lista[2]) or sorted(lista[1]) == sorted(lista[2]):
        nuevalista = [lista[0], lista[1]]
        print(nuevalista)

    else:
        print(lista)

anagramas_unicos(["isla", "pan", "lisa"])