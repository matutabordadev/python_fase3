nombre = input("Digame su nombre porfavor:  ")
print("Bienvenido/a", nombre)
while True:
    print("\n--- MENU PRINCIPAL ---")
    print("1"," - Verificar edad")
    print("2"," - Mostrar mensaje")
    print("3"," - Salir")
    opcion = input("Elegí una opción:  ")
    if opcion == "1":
        print("\nElegiste verificar edad")
        while True:
            edad = input("¿Que edad tiene?  ")
            if not edad.isdigit(): # Verifica si es número
                print("Error: ingrese solo números.")
                continue
            edad_numero = int(edad)
            if edad_numero <1 or edad_numero >120:
                    print("Edad invalida. Ingrese un numero entre 1 y 120")
                    continue
            break # Edad válida
        if edad_numero <17:
            print("Acceso denegado, edad no permitida")
        elif edad_numero ==17:
            print("Acceso denegado, tenes", edad_numero, ", el año proximo cumpliras", edad_numero+1, "y podras acceder")
        else:
            print("Acceso permitido, sea bienvenido")      
    elif opcion == "2":
        print("Estamos verificando su edad para validar su ingreso, si no quire hacerlo, salga del sistema")
    elif opcion == "3":
        print("Saliendo del programa.. Hasta luego", nombre)
        break
    else:
        print("Opción inválida, ingrese una opcion valida 1,2,3")
