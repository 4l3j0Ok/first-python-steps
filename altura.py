def calc_altura():

    nombre1 = (input("Indique el nombre de la primer persona: "))
    altura1 = float(input("Indique su altura: "))
    nombre2 = (input("Indique el nombre de la segunda persona: "))
    altura2 = float(input("Indique su altura: "))
    
    if altura1 > altura2:
        print ("La persona más alta es:", nombre1)

    else:
        print ("La persona más alta es:", nombre2)

calc_altura()