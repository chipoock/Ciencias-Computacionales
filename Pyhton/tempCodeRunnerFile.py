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
