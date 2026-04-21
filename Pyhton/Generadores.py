def generadorPares(Limite):
    
    num = 1
    while num<Limite:
    #yield se utiliza como lista recorre uno a la vez y ahorra espacio al recorrer la funcion
        yield num*2
        num += 1

devuelvePares = generadorPares(11)

print(next(devuelvePares))
print("Mas codigo")
print(next(devuelvePares))
print("Mas codigo")
print(next(devuelvePares))
print("Mas codigo")
