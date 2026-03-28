estudiantes = {
    "Anna": 8,
    "Luis": 9,
    "Maria": 7
}
while True:
    print ("-----MENÚ-----")
    print("1. Agregar estudiante")
    print("2. Mostrar estudiantes")
    print("3. Buscar estudiante")
    print("4. Eliminar estudiante")
    print("5. Salir")
    opcion = input("Seleccione un número: ")
    if opcion == "1":
        nombre = input("Ingrese el nombre del estudiante: ")
        calificacion = float(input("Ingrese la calificación del estudiante: "))
        estudiantes[nombre] = calificacion
        print("DEBUG:", estudiantes)
    elif opcion == "2":
        print("------- Lista de estudiantes y sus calificaciones -------")
        for nombre, calificacion in estudiantes.items():
            print(nombre, ":", calificacion)
    elif opcion == "3":
        buscar = input("Nombre del estudiante a buscar:")
        if buscar in estudiantes:
            print(f"{buscar} tiene una calificación de {estudiantes[buscar]}.")
        else:
            print(f"Estudiante {buscar} no encontrado.")
    elif opcion == "4":
        eliminar = input("Nombre del estudiante a eliminar:")
        if eliminar in estudiantes:
            del estudiantes[eliminar]
            print(f"Estudiante {eliminar} eliminado.")
        else:
            print(f"Estudiante {eliminar} no encontrado.")
    elif opcion == "5":
        print("Saliendo del programa.")
        break
    else:        print("Opción no válida. Por favor, seleccione un número del 1 al 5.")