while True:
    print("\n\n\n__________Menu__________"
    "\n Act.1 Dicionario de cuadrado"
    "\n Act.2 Precio de Frutas" 
    "\n Act.3 Diccionario Datos" 
    "\n Act.4 Diccionario Agenda" 
    "\n Num.5 SALIR")
    Menu = int(input("Introduce un numero para continuar: "))
    print("\n\n\n\n")
    #Act.1 Dicionario de cuadrado
    if Menu == 1:
        print("-----Diccionario de Cuadrado-----")
        Numero = int(input("Introduce un numero: "))
        Cuadrados = {
            Numeros_Clave : Numeros_Clave**2 for Numeros_Clave in range(1,Numero +1 )
        }
        print(Cuadrados)
    #Act.2 Precio de Ftrutas
    elif Menu == 2:
        Frutas_y_Precios = {
            "MANZANA" : 40, 
            "PERA" : 60,
            "PLATANO" : 24,
            "MELON": 26,
            "GUAYABA" : 50
        } 
        Fruta_Cliente = str(input("Introduce la fruta a comprar: ")).upper()
        Fruta_Kilos = int(input("Introduce los Kg a comprar: "))
        if Fruta_Cliente in Frutas_y_Precios:
            Precio_Total = Frutas_y_Precios[Fruta_Cliente] * Fruta_Kilos
            print(f"El precio de {Fruta_Kilos}Kg de {Fruta_Cliente} es: {Precio_Total}")
        else:
            print(f"La fruta {Fruta_Cliente} no se encuentra en la tienda")
    #Diccionario Datos
    elif Menu == 3:
        Persona = {}
        Lista_Datos = ["Nombre","Edad","Sexo","Telefono","Correo Electronico"]
        for Dato in Lista_Datos:
            Valor = str(input(f"Introduce tu {Dato}: "))
            Persona[Dato] = Valor
            print("\n\n ____Contenido de el diccionario____")
            print(Persona)
            print("_" * 40)
    #Diccionario Agenda
    elif Menu == 4:
        agenda = {}
        while True:
            print("\n_____AGENDA TELEFÓNICA_____")
            print("1. Añadir/Modificar contacto")
            print("2. Buscar contacto")
            print("3. Borrar contacto")
            print("4. Listar contactos")
            print("5. Salir")
            Opcion = input("Introduce un numero para continuar: ").strip()
            if Opcion == "1":
                nombre = input("\n\n Introduce el nombre del contacto: ").strip()
                if nombre in agenda:
                    print(f"\n\nEl número actual de {nombre} es {agenda[nombre]}")
                    modificar = input("Deseas modificarlo? (SI/NO): ").lower()
                    if modificar == "s":
                        Nuevo_Numero = input("Introduce el nuevo número: ")
                        agenda[nombre] = Nuevo_Numero
                        print("Contacto actualizado.")
                else:
                    numero = input("Introduce el numero de teléfono: ")
                    agenda[nombre] = numero
                    print("Contacto añadido.")
            elif Opcion == "2":
                cadena = input("Introduce el inicio del nombre a buscar: ").strip()
                encontrados = False
                for nombre in agenda:
                    if nombre.startswith(cadena):
                        print(f"{nombre}: {agenda[nombre]}")
                        encontrados = True
                if not encontrados:
                    print("No se encontraron contactos.")
            elif Opcion == "3":
                nombre = input("Introduce el nombre del contacto a borrar: ").strip()
                if nombre in agenda:
                    confirmar = input(f"¿Estás seguro de que deseas borrar a {nombre}? (s/n): ").lower()
                    if confirmar == 's':
                        del agenda[nombre]
                        print("Contacto borrado.")
                else:
                    print("Ese contacto no existe.")
            elif Opcion == "4":
                if agenda:
                    print("Lista de contactos:")
                    for nombre, numero in agenda.items():
                        print(f"{nombre}: {numero}")
                else:
                    print("La agenda está vacía.")
            elif Opcion == "5":
                print("Saliendo de la agenda")
                break
            else:
                print("Opción no válida. Intenta de nuevo.")
    elif Menu == 5:
        break
    else:
        print("El numero introducido no es valido :(( ")