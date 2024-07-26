def switch_case(miprograma):
    pedro = {
        1: "Seleccionaste la opción 1: Cocinar: Pollo y papas",
        2: "Seleccionaste la opción 2: Jugar: Fútbol y Basqutbal",
        3: "Seleccionaste la opción 3: Dormir en una cama",
        4: "Seleccionaste Salir del programa",
}
    return pedro.get(miprograma, "opción no valida")

def main():
    print("Selecciona una opción: ")
    print("La opción 1 es: Cocinar ")
    print("La opción 2 es: Jugar ")
    print("La opción 3 es: Descansar ")
    print("Opción 4 Salir")
    
    try:
        opcion = int(input("Ingresa una opción entre (1-4): "))
        resultado = switch_case(opcion)
        print(resultado)
    except ValueError:
        print("Por favor, debes ingresar un número válido.")
main()
    