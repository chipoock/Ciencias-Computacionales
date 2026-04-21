
def divide():
    try:
        op1 = float(input("Introduce el primer numero: "))
        op2 = float(input("Intoduce el segundo numero: "))
        print(f"La division es: {op1/op2}")
    except ValueError:
        print("El valor no es correcto")
    except ZeroDivisionError:
        print(" ERROR No se puede dividir entre  :((")
    
    finally:
        print("el programa a finalizado :) ")

divide()