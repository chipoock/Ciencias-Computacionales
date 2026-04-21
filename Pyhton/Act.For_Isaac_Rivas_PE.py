while True:
    print("\n\n\n_____________ Menu _____________"
    "\nAct.1 Mayor,Menor o igual a cero"
    "\nAct.2 Tabla de Multiplicar"
    "\nAct.3 Ahorro en el año"
    "\nAct.4 Salario de la semana"
    "\nAct.5 Deuda a pagar"
    "\nSalir(6)")
    #Act.1 Mayor,Menor o igual a cero
    Menu = int(input("Introduce un numero para continuar: "))
    if Menu == 1: 
        Numeros_Introducir = int(input("Cunatos numeros deseas introducir? "))
        Mayores_Cero = 0
        Menores_Cero = 0
        Iguales_Cero = 0
        for i in range(Numeros_Introducir):
            Cantidad = int(input(f"Introduce el numero {i+1}: "))
            if Cantidad > 0:
                Mayores_Cero += 1
            elif Cantidad < 0:
                Menores_Cero += 1
            else:
                Iguales_Cero += 1
        print(f"\nNumeros mayores a 0 son: {Mayores_Cero}")
        print(f"Numeros menores a 0 son: {Menores_Cero}")
        print(f"Numeros iguales a 0 son: {Iguales_Cero}")
    #Act.2 Tabla de Multiplicar
    elif Menu == 2:
        print("...Tabla de multiplicar...")
        Tabla = int(input("Introduce el numero al que quieres que llegue la tabla: "))
        for n in range(1,(Tabla + 1)):
            print(f"\n____Tabla de Multiplicar del {n}____")
            for i in range(1,11):
                Resultado = i * n
                print(F"{n} X {i} = {Resultado}")
    #Act.3 Ahorro en el año
    elif Menu == 3:
        Ahorro_Total = 0
        for i in range(12):
            print(f"\n\n____MES {i + 1}___")
            Ahorro_Mes = int(input("Intoduce la cantidad a ahorrar: "))
            Ahorro_Total += Ahorro_Mes
            print(f"llevas ahorrado {Ahorro_Total} este mes")
        print(f"El total ahorrado en el año es: {Ahorro_Total}")
    #Act.4 Salario de la semana
    elif Menu == 4:
        Lista_Dias_Semana = ["Lunes","Martes","Miercoles","Jueves","Viernes","Sabado"]
        Pago_Semanal = 0
        for i in Lista_Dias_Semana:
            print(f"\n\n_____Dia {i}_____")
            Horas_Trabajadas = float(input("Introduce las horas trabajadas hoy: "))
            Pago_Minimo = 34.85
            Pago_Semanal = Pago_Semanal + (Horas_Trabajadas * Pago_Minimo)
        print(f"Tu sueldo de esta semana es: {Pago_Semanal}")
    #Act.5 Deuda a pagar
    elif Menu == 5:
        Deuda = 10
        Total_Pagado = 0
        for i in range(0,41,2):
            Deuda_Incremento = Deuda * i
            print(f"Mes {int(i/2)}: {Deuda_Incremento}$")
            Total_Pagado = Total_Pagado + Deuda_Incremento
        Total_Pagado += 10
        print(f"El total a pagar despues de los 20 meses es: {Total_Pagado}")
    elif Menu == 6:
        break
    else:
        print("El numero intoducido no es valido :( "
        "\nIntroduce un numero del 1 al 6")
    Lista_SN = ["si","no"]
    Finalizar_Programa = str(input("\nQuieres Regresar al menu? (Si/No)"))
    if Finalizar_Programa.lower() in Lista_SN[0]:
        print("Regresando...")
    elif Finalizar_Programa in Lista_SN[1]:
        break
    else:
        print("No has introducido si o no en el programa")