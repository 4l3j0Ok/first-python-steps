import datetime

print(datetime.datetime.today())

print(datetime.timedelta(minutes=100))

#También se puede importar desde un módulo un método específico de él, por ejemplo:
from datetime import timedelta
#Entonces puedo usar el método timedelta sin necesidad de llamar a datetime:
print(timedelta(minutes=200))

#Utilización de módulo propio

from mymodule import suma, resta

suma(50, 55)
resta(100, 50)