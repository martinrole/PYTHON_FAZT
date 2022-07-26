## Mis propios modulos
### Forma 1 de importar
import misModulos

misModulos.agregar(2,3)

### Forma 2 de importar
from misModulos import restar

restar(5,5)

## Modulos descargados de otros desarrolladores:
###Buscar modulos en la pagina pypi.org e instalar el deseado
from colorama import Fore, Style, init

init(convert=True)
print( Fore.RED + "Texto Personalizado")



## Modulos de python
from datetime import timedelta, date

### Muestra la fecha actual
print( date.today() )

### Convierte numeros a formato tiempo:
print( timedelta( minutes=70) ) 