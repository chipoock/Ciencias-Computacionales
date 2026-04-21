x = 0
while x <= 0:
    print("\n                __Menu__")
    Entrada_Menu = int(input("--- Area y Perimetro del rectangulo(1) \n--- Triángulo rectángulo(2) \n--- Operaciones Basicas(3) "
    "\n--- Grados Fahrenheit a Celsius(4) \n--- Calcula la media(5) \n--- Minutos a horas(6) \n--- Descuento de Tienda(7)"
    "\n--- Numeros Invertidos(8) \n--- Mostrar Iniciales(9) \n--- Puntos en el plano(10) \n--- Salir(11) \nIntroduce un numero para continuar: "))
    #Ejercicio 1 Area y perimetro de un Rectangulo
    if Entrada_Menu == 1 :
        print("\nArea y perimetro de un rectangulo")
        Seleccion = int(input(" .-Area(1) \n .-Perimetro(2): "))
        if Seleccion == 1: 
            print("\n-Calcula el area del rectangulo")
            Base_Rectangulo = int(input("Introduce la base: "))
            Altura_Rectangulo = int(input("Introduce la altura: "))
            Respuesta = Base_Rectangulo * Altura_Rectangulo
            print("El area es:",Respuesta)
        else:
            print("\n-Calcula el Perimetro del Rectangulo")
            Base_Rectangulo = int(input("Introduce la base: "))
            Altura_Rectangulo = int(input("Introduce la altura: "))
            Respuesta = Altura_Rectangulo * 2 + Base_Rectangulo * 2 
            print("El perimetro del rectangulo es: ", Respuesta)
    #Ejercicio 2 Hipotenusa de Triangulo Rectangulo
    elif Entrada_Menu == 2 :
        print("\nHipotenusa del Triangulo Rectangulo")
        Cateto_1 = int(input("Intoduce eL cateto 1: ")) 
        Cateto_2 = int(input("Intoduce eL cateto 2: ")) 
        Respuesta = Cateto_1 * Cateto_1 + Cateto_2 * Cateto_2
        print("La hipotenusa es: ", Respuesta)
    #Ejercicio 3 Operaciones Basicas
    elif Entrada_Menu == 3 :
        print("\n ---Operaciones Basicas---")
        Numero_1 = int(input("Introduce el primer numero: "))
        Numero_2 = int(input("Introduce el segundo numero: "))
        Respuesta = 0
        print("\nElige una operacion")
        Menu_Operaciones_Basicas = int(input(" .-Suma(1) \n .-Resta(2) \n .-Multiplicacion(3) \n .-Division(4) \n Introduce un numero del 1 al 4 para continuar: "))
        if Menu_Operaciones_Basicas == 1:
            Respuesta = Numero_1 + Numero_2
            print(" La suma es: ", Respuesta)
        elif Menu_Operaciones_Basicas == 2:
            Respuesta = Numero_1 - Numero_2
            print(" La Restas es: ", Respuesta)
        elif Menu_Operaciones_Basicas == 3:
            Respuesta = Numero_1 * Numero_2
            print(" La Multiplicacion es: ", Respuesta)
        elif Menu_Operaciones_Basicas == 4:
            Respuesta = Numero_1 / Numero_2
            print(" La Division es: ", Respuesta)
        else :
            print("El numero que ingreso no es valido")
    #Ejercicio 4 grados Fahrenheit a grados Celsius
    elif Entrada_Menu == 4:
        print("\n  Grados Fahrenheit a Celsius")
        Grados_F = float(input("Introduce los grados Fahrenheit: "))
        Respuesta = Grados_F - 32
        Respuesta *= 0.5556
        print("Los grados Fahrenheit a Celsius son: ",Respuesta)
    #Ejercicio 5 Calcula la media de tres números
    elif Entrada_Menu == 5:
        print("\n   Calcula la media")
        Num_1 = int(input("Ingresa el primer numero: "))
        Num_2 = int(input("Ingresa el segundo numero: "))
        Num_3 = int(input("Ingresa el tercer numero: "))
        Respuesta = Num_1 + Num_2 + Num_3
        Respuesta /= 3
        print("La media de los tres numeros es: ",Respuesta)
    #Ejercicio 6 Minutos a horas
    elif Entrada_Menu == 6:
        print("\nMinutos a horas")
        Num_Minutos = int(input("Introduce el numero de minutos: "))
        Respuesta = Num_Minutos / 60
        Nueva_Respuesta = int(Respuesta)
        Num_Minutos %= 60
        print(Nueva_Respuesta,"Horas y",Num_Minutos,"Minutos")
    #Ejercicio 7 Descuento de la tienda
    elif Entrada_Menu == 7:
        print("\n Tienda de productos")
        Total_Compra = int(input("Introduce el total a pagar: "))
        descuento = 0.15
        Resultado = Total_Compra - (Total_Compra * descuento)
        print("El precio final a pagar es: ",Resultado)
    #Ejercicio 8 Numeros invertidos
    elif Entrada_Menu == 8:
        print("\n  Numero Invertidos")
        Numero_Invertido = int(input("Ingresa el numero de dos cifras: "))
        if 10 <= Numero_Invertido <= 99:
            invertido = (Numero_Invertido % 10) * 10 + (Numero_Invertido // 10)
            print(f"El número invertido es: {invertido}")
        else:
                print("El número ingresado no tiene dos cifras.")
    #Ejercicio 9 Tomar iniciales de apellidos y nombre 
    elif Entrada_Menu == 9:
        print("\n   Mostrar Iniciales")
        Nombre = input("introduce tu nombre: ")
        Primer_Apellido = input("Introduce tu primer apellido: ")
        Segundo_Apellido = input("Introduce tu segundo apellido: ")
        Iniciales = Nombre[0].upper() + Primer_Apellido[0].upper() + Segundo_Apellido[0].upper()
        print(f"Las iniciales son: {Iniciales}")
    #Ejercicio 10 Representar puntos en el plano
    elif Entrada_Menu == 10:
        import math
        print("\n  Representa dos puntos en el plano")
        Num1_x = float(input("Ingresa la coordenada x1: "))
        Num1_y= float(input("Ingresa la coordenada y1: "))
        Num2_x = float(input("Ingresa la coordenada x2: "))
        Num2_y = float(input("Ingresa la coordenada y2: "))
        Distancia = math.sqrt((Num2_x - Num1_x)**2 + (Num2_y - Num1_y)**2) 
        print(f"La distancia entre los puntos es: {Distancia:.2f}")
    elif Entrada_Menu == 11:
        break
    else:
        print("El numero que ingresaste no es valido")