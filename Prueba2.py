def menu():
    print("Menú Principal")
    print("1. Opción 1")
    print("2. Opción 2")
    print("3. Opción 3")
    print("4. Salir")

def opcion1():
    print("Has seleccionado la Opción 1")

def opcion2():
    print("Has seleccionado la Opción 2")

def opcion3():
    print("Has seleccionado la Opción 3 Bienvenido")
    h = 3+5
    print(h)

def main():
    while True:
        menu()
        opcion = input("Selecciona una opción : ")#Se borra lineas vacias
        if opcion == '1':
            opcion1()
        elif opcion == '2':
            opcion2()
        elif opcion == '3':
            opcion3()
        elif opcion == '4':
            print("Saliendo...")
            break
        else:
            print("Opción no válida, por favor selecciona una opción válida.")

if __name__ == "__main__":
    main()