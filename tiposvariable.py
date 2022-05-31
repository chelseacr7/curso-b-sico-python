# Strings - Cadena de texto, o sea palabras
from cgi import print_arguments
from cmath import pi


nombre = "Chelsea"

#Enteros - Números sin punto decimal
edad = 23 
edads = "26"

#Ejemplo
print(edad+edad)
print(edads+edads)

#Flotante - Número con punto decimal
pi = 3.1416

#Transformacion de entero a flotante
edad = float(edad) #Casteo: Conversion de una variable a otra

#Usa type para saber de qué tipo es la variable
print(type(nombre), type(edad))

#Bool o Booleano - Este unicamente puede ser SI O NO
tegusto = False
tegusto = True

print(tegusto)