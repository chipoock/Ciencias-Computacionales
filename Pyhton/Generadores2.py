#  ------yiedl from-------
#Utilidad: Simplificar el codigo de los generadores en el caso de utilizar
#bucles anidados
def devuelve_ciudades(*ciudades):
    for elemento in ciudades:
        #for subElemento in elemento:
        yield from elemento
ciudades_devueltas = devuelve_ciudades("Zapopan","guadalajara","Monterrey","Michoacan")
print(next(ciudades_devueltas))
print(next(ciudades_devueltas))
