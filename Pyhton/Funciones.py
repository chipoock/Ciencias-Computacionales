while True:
    print("___________MENU__________" \
    "\n Act.1 Funcion Nombre" \
    "\n Act.2 Calcular Iva" \
    "\n Act.3 Area Circulo" \
    "\n Act.4 Login")
    Menu = int(input("Introduce un numero para continuar: "))
    #Act.1 Funcion Mandar a llamar el nombre
    if Menu == 1:
        def Saludo(Nombre):
            print(f"Hola {Nombre}")
        Nombre = str(input("Introduce tu nombre: "))
        Saludo(Nombre)
    #Act.2 Calcular Iva
    elif Menu == 2 :
        def Calcular_Total(Cantidad, Porcentaje_Iva=16):
            Total = Cantidad * (1 + Porcentaje_Iva / 100)
            return Total
        Cantidad = float(input("Introduce la cantidad sin IVA: "))
        Total = Calcular_Total(Cantidad, Porcentaje_Iva=16) 
        print(f"El total de la factura con IVA es: {Total}")
    #Act.3 Area Circulo
    elif Menu == 3:
        import math
        def area_circulo(radio):
            return math.pi * radio ** 2
        def volumen_cilindro(radio, altura):
            area_base = area_circulo(radio)
            return area_base * altura
        radio = float(input("Ingresa el radio del círculo (en unidades): "))
        altura = float(input("Ingresa la altura del cilindro (en unidades): "))
        print(f"\nÁrea del círculo: {area_circulo(radio):.2f}")
        print(f"Volumen del cilindro: {volumen_cilindro(radio, altura):.2f}")
    #Act.4 Login
    elif Menu == 4:
        def login(nombre_usuario, contrasena, intentos):
            if nombre_usuario == "usuario1" and contrasena == "asdasd":
                return True, intentos
            else:
                intentos += 1
                return False, intentos
        intentos = 0
        MAX_INTENTOS = 3
        while intentos < MAX_INTENTOS:
            usuario = input("Nombre de usuario: ")
            password = input("Contraseña: ")
            exito, intentos = login(usuario, password, intentos)
            if exito:
                print(" Login exitoso. ¡Bienvenido!")
                break
            else:
                print(f" Usuario o contraseña incorrectos. Intento {intentos} de {MAX_INTENTOS}.\n")
        if intentos == MAX_INTENTOS:
            print(" Has superado el número máximo de intentos. Acceso denegado.")

