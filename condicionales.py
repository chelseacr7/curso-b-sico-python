calificacion = input("Introduce tu calificación de la AZ 900: ")
calificacion = int (calificacion)

if calificacion < 700 : 
    print("Por no estudiar, Chels, te dije")
elif calificacion > 1000 :
    print("Inválido")
else :
    print("Obvio lo ibas a pasar, eres una chingona")


edad = input("Introduce tu edad: ")
edad = int(edad)

if edad >= 18 and edad <= 100 :
    print("Bienvenide")
elif edad > 100 :
    print("Lo siento, acceso denegado")
elif edad <= 0 :
    print("Inválido")
else :
    print("Acceso denegado")