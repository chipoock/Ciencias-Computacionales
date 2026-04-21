x = True
while x == True:
    print("\n\n___________________Menu____________________"
    "\n....Act.1 - Tiempo de llamada Telefonica"
    "\n....Act.2 - Las Caras de un dado"
    "\n....Act.3 - Indica el dia de la semana"
    "\n....Act.4 - Dias que tienen los meses"
    "\n....Act.5 - Calcula el precio del paquete"
    "\n....Salir (6)")
    Menu = int(input("Introduce un numero del 1 al 6 para continuar:"))
    #Act.1 Tiempo de llamada Telefonica
    if Menu == 1:
        Tiempo_Llamada = int(input("Introduce el Tiempo que duro la llamada: "))
        Dia_Semana = str(input("Introduce el dia que hizo la llamada: "))
        Turno = str(input("Introduce el Turno (Mañana / Tarde) que hizo la llamada: "))
        Dias_Semana_Lista = ["Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"]
        Turno_Lista = ["Mañana","Tarde"]
        Cinco_Minutos = 1
        Tres_Minutos = 0
        Dos_Minutos = 0
        Un_Minuto = 0
        Total_Pago = 0
        if Tiempo_Llamada <= 5:
            Cinco_Minutos = 1
        elif 6 <= Tiempo_Llamada <= 8:
            Cinco_Minutos = 1
            Tres_Minutos = 0.80 * (Tiempo_Llamada - 5) 
            Total_Pago = Cinco_Minutos + Tres_Minutos
        elif  9<= Tiempo_Llamada <=10:
            Cinco_Minutos = 1
            Tres_Minutos = 0.80 * 3  
            Dos_Minutos = 0.70 * (Tiempo_Llamada - 8)  
            Total_Pago = Cinco_Minutos + Tres_Minutos + Dos_Minutos
        elif 10 <= Tiempo_Llamada <= 100:
            Cinco_Minutos = 1
            Tres_Minutos = 0.80 * 3 
            Dos_Minutos = 0.70 * 2   
            Un_Minuto = 0.50 * (Tiempo_Llamada - 10) 
            Total_Pago = Cinco_Minutos + Tres_Minutos + Dos_Minutos + Un_Minuto
        if Dia_Semana == Dias_Semana_Lista[6]:
            Total_Pago = Total_Pago - (Total_Pago * (3 / 100))
        else:
            if Turno == Turno_Lista[0]:
                Total_Pago = Total_Pago - (Total_Pago * (15 / 100))
            elif Turno == Turno_Lista[1]:
                Total_Pago = Total_Pago - (Total_Pago * (10 / 100))
            else:
                print("El Turno ingresado no existe")
        print(f"El costo de la llama es: {Total_Pago} euros")
    #Act.2 Las Caras de un dado
    elif Menu == 2:
        Dado_Entrada = int(input("Ingresa el numero de la cara del dado (1-6): "))
        if Dado_Entrada == 1:
            print("la cara opuesta es 6")
        elif Dado_Entrada == 2:
            print("La cara opuesta es 5")
        elif Dado_Entrada == 3:
            print("La cara opuesta es 4")
        elif Dado_Entrada == 4:
            print("La cara opuesta es 3")
        elif Dado_Entrada == 5:
            print("La cara opuesta es 2")
        elif Dado_Entrada == 6:
            print("La cara opuesta es 1") 
        else:
            print("El numero ingresado no es una cara del dado")  
    #Act.3 Indica el dia de la semana
    elif Menu == 3:
        Dia_Semana = int(input(".............Teniendo en cuenta que 1 es lunes y 7 es domingo"
                            "\n.....................Ingresa un numero del 1 al 7 :"))
        Lista_Dias_Semana = ["lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"]
        if Dia_Semana == 1 :
            print(f"El dia es: {Lista_Dias_Semana[0]} ")
        elif Dia_Semana == 2 :
            print(f"El dia es: {Lista_Dias_Semana[1]} ")
        elif Dia_Semana == 3 :
            print(f"El dia es: {Lista_Dias_Semana[2]} ")
        elif Dia_Semana == 4 :
            print(f"El dia es: {Lista_Dias_Semana[3]} ")
        elif Dia_Semana == 5 :
            print(f"El dia es: {Lista_Dias_Semana[4]} ")
        elif Dia_Semana == 6 :
            print(f"El dia es: {Lista_Dias_Semana[5]} ")
        elif Dia_Semana == 7 :
            print(f"El dia es: {Lista_Dias_Semana[6]} ")
        else:
            print("El numero que introducido no corresponde a un dia de la semana")
    #Act.4 Dias que tienen los meses
    elif Menu == 4:
        Dias_Mes = int(input("Introduce el numero del mes: "))
        Lista = ["Enero","Febrero","Marzo","Abril","Mayo","Junio"
        ,"Julio","Agosto","Septiembre","Octubre","Noviembre","Dicimbre"]
        Lista2 = [28,30,31]
        if Dias_Mes == 1:
            print(f"{Lista[0]} Tiene {Lista2[2]} Dias")
        elif Dias_Mes == 2:
            print(f"{Lista[1]} Tiene {Lista2[0]} Dias")
        elif Dias_Mes == 3:
            print(f"{Lista[2]} Tiene {Lista2[2]} Dias")
        elif Dias_Mes == 4:
            print(f"{Lista[3]} Tiene {Lista2[1]} Dias")
        elif Dias_Mes == 5:
            print(f"{Lista[4]} Tiene {Lista2[2]} Dias")
        elif Dias_Mes == 6:
            print(f"{Lista[5]} Tiene {Lista2[1]} Dias")
        elif Dias_Mes == 7:
            print(f"{Lista[6]} Tiene {Lista2[2]} Dias")
        elif Dias_Mes == 8:
            print(f"{Lista[7]} Tiene {Lista2[2]} Dias")
        elif Dias_Mes == 9:
            print(f"{Lista[8]} Tiene {Lista2[1]} Dias")
        elif Dias_Mes == 10:
            print(f"{Lista[9]} Tiene {Lista2[2]} Dias")
        elif Dias_Mes == 11:
            print(f"{Lista[10]} Tiene {Lista2[1]} Dias")
        elif Dias_Mes == 12:
            print(f"{Lista[11]} Tiene {Lista2[2]} Dias")
        else:
            print("El numero introducido no es del 1 al 12")
    #Act.5 Calcula el precio del paquete
    elif Menu == 5:
        Peso_Paquete = int(input("Introduce el peso en kg del paquete: "))
        Lista_Direccion = ["America del Norte","America Central","America del Sur","Europa","Asia"]
        Resultado = 0
        print("_____DIRECIONES DISPONIBLES_____"
        "\n....America del Norte"
        "\n....America Central"
        "\n....America del Sur"
        "\n....Europa"
        "\n....Asia")
        Direccion = str(input("\nIntroduce la direcion a la que va el paquete: "))
        if Peso_Paquete <= 5:
            if Direccion == Lista_Direccion[0]:
                Resultado = 1 * Peso_Paquete
            elif Direccion == Lista_Direccion[1]:
                Resultado = 2 * Peso_Paquete
            elif Direccion == Lista_Direccion[2]:
                Resultado = 5 * Peso_Paquete
            elif Direccion == Lista_Direccion[3]:
                Resultado = 15 * Peso_Paquete
            elif Direccion == Lista_Direccion[4]:
                Resultado = 18 * Peso_Paquete
            else:
                print("EL peso supera nuestra politica(Intente que sea igual o menor a 5kg)")
        print(f"El precio a pagar es: {Resultado} pesos")
    elif Menu == 6:
        break
    else:
        print("El Numero no es valido (intente con un numero del 1 al 6")
