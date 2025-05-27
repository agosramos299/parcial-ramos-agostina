from funciones.opciones_menu import mostrar_menu
from funciones.pacientes import cargar_pacientes, mostrar_pacientes, buscar_por_historia
from funciones.ordenamiento import ordenar_por_historia
from funciones.estadisticas import paciente_mas_dias, paciente_menos_dias, contar_mas_de_5_dias, promedio_dias
from funciones.validaciones import pedir_entero


pacientes = []
opcion = 0

while opcion != 9:
    mostrar_menu()
    opcion = pedir_entero("Seleccione una opción: ", minimo=1)
    
    if len(pacientes) == 0 and opcion != 1 and opcion != 9:
        print("No hay pacientes cargados.")
        continue

    match opcion:
        case 1:
            pacientes = cargar_pacientes()
        case 2:
            mostrar_pacientes(pacientes)
        case 3:
            buscar_por_historia(pacientes)
        case 4:
            ordenar_por_historia(pacientes)
            print("Pacientes ordenados.")
        case 5:
            paciente_mas_dias(pacientes)
        case 6:
            paciente_menos_dias(pacientes)
        case 7:
            contar_mas_de_5_dias(pacientes)
        case 8:
            promedio_dias(pacientes)
        case 9:
            print("Saliendo...")
        case _:
            print("Opción inválida.")

