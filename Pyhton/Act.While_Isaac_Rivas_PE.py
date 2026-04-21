while True:
    print("\n\n\n________________ Menu _______________"
    "\n....Act.1 Suma de numeros siclo while"
    "\n....Act.2 Vocales"
    "\n....Act.3 Desea terminar el programa"
    "\n....Act.4 Introduce Contraseña"
    "\n....Act.5 Alcancia digital"
    "\n....Salir(6)")
    #Act.1 Suma los numeros hasta que se introdusca un 0
    Menu = int(input("Introduce un numero para continuar: "))
    if Menu == 1:
        Suma = 0
        Contador = 0
        X = 0
        while True:
            Numero = int(input("Introduce un numero(0 para terminar): "))
            Suma += Numero
            Contador += 1
            if Numero == 0:
                break
            if Contador > 0:
                Promedio = Suma / Contador
        print(f"La suma de los numeros es: {Suma}")
    #Act.2 Vocales
    elif Menu == 2:
        Lista_Vocal = ["a","e","i","o","u"]
        while True:
            print("\n(Introduce espacio para salir)")
            Vocal_Usuario = str(input("Introduce un Carácter: "))
            if Vocal_Usuario.lower() in Lista_Vocal:
                print(f"{Vocal_Usuario} Es una vocal")
            elif Vocal_Usuario == " ":
                break
            else:
                print(f"{Vocal_Usuario} No es una vocal")
    #Act.3 Desea terminar el programa
    elif Menu == 3:
        while True:
            Lista_Para_Finalizar = ["s"]
            print("____Bienvenido a la Actividad 3____")
            Finalizar = str(input("Desea terminar el programa? \n"
            "Introduce (S para termiar) cualquier tecla para continuar: "))
            if Finalizar.lower() in Lista_Para_Finalizar:
                break
    #Act.4 Introduce Contraseña
    elif Menu == 4:
        print("____Ingreso de Usuario____")
        Contraseña_Usuario = str(input("Introduce una contraseña: "))
        x = 0
        Intentos = 4
        while x < Intentos:
            print("...Verificacion de Contraseña")
            Validacion_Contraseña = str(input("...Introduce la contraseña para continuar: "))
            x += 1
            Validacion_Intentos = Intentos - x
            if Contraseña_Usuario == Validacion_Contraseña:
                print("La Contraseña es correcta")
                break
            else:
                print(f"\nLas contraseñas no coinciden (Te quedan {Validacion_Intentos} intento/s)")
    #Act.5 Alcancia digital
    elif Menu == 5:
        print("\n__________________ALCANCIA DIGITAL__________________")
        Ahorro_Meta = int(input("Introduce la cantidad de dinero que quieres ahorrrar: "))
        Ahorro_Total = 0
        x = 0
        while x <= 0:
            Ahorro_Ingresado = int(input("Introduce la cantidad que deseas meter a la alcancia: "))
            if Ahorro_Ingresado > 0:
                Ahorro_Total += Ahorro_Ingresado 
                if Ahorro_Total >= Ahorro_Meta:
                    Ahorro_Final = str(input("Has llegado a tu meta. Deseas continuar ahorrando?"
                    "Introduce (SI/NO) para continuar: "))
                    Lista_SN = ["si","no"]
                    if Ahorro_Final.lower() == Lista_SN[0]:
                        Ahorro_Verificacion = Ahorro_Total - Ahorro_Meta
                        print(f"\nllevas ahorrodo sobre tu meta la cantidad de {Ahorro_Verificacion}$ y en total tienes {Ahorro_Total}$ ")
                    elif Ahorro_Final == Lista_SN[1]:
                        x = 1
                    else:
                        print("Intoduce un Si o No para continuar")
            else:
                print("No puedes ingresar numeros negativos")
        print(f"El total ahorrado fue {Ahorro_Total}$")
    elif Menu == 6:
        break
    else:
        print("El numero intoducido no es valido :( "
        "\nIntroduce un numero del 1 al 6")
    Lista_SN2 = ["si","no"]
    Finalizar_Programa = str(input("\nQuieres Regresar al menu? (Si/No)"))
    if Finalizar_Programa.lower() in Lista_SN2[0]:
        print("Regresando...")
    elif Finalizar_Programa in Lista_SN2[1]:
        break
    else:
        print("No has introducido si o no en el programa")


