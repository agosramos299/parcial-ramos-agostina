from funciones.validaciones import pedir_entero
def cargar_pacientes() -> list[list]:
    """
    Solicita al usuario los datos de una cantidad determinada de pacientes y los almacena en una lista.

    Por cada paciente se solicita: número de historia clínica, nombre, edad, diagnóstico y días de internación.

    Returns:
        list[list]: Lista de pacientes donde cada uno es representado como una lista de 5 elementos.
    """

    cantidad = pedir_entero("¿Cuántos pacientes desea ingresar? ", minimo=1)

    lista = []

    for i in range(cantidad):
        print(f"\nPaciente {i+1}")
        historia = int(input("Número de historia clínica: "))
        nombre = input("Nombre del paciente: ")
        edad = int(input("Edad del paciente: "))
        diagnostico = input("Diagnóstico del paciente: ")
        dias = int(input("Días de internación del paciente: "))
        paciente = [historia, nombre, edad, diagnostico, dias]
        lista += [paciente]
    return lista

def mostrar_pacientes(pacientes: list[list]):
    """
    Muestra por consola la información de todos los pacientes de la lista.

    Args:
        pacientes (list): lista de pacientes

    """
    
    for paciente in pacientes:
        print(f"N° de Historia: {paciente[0]} | Nombre: {paciente[1]} | Edad: {paciente[2]} | Diagnóstico: {paciente[3]} | Días: {paciente[4]}")


def buscar_por_historia(pacientes: list):
    """
    Permite buscar pacientes por número de historia clínica. 
    Si no se encuentra, ofrece la posibilidad de reintentar.

    Args:
        pacientes (list): lista de pacientes

    """
    seguir = 1
    while seguir == 1:
        historia = int(input("Ingrese número de historia clínica a buscar: "))
        encontrado = False


        for i in range(len(pacientes)):
            if pacientes[i][0] == historia:
                print(f"Historia: {pacientes[i][0]} | Nombre: {pacientes[i][1]} | Edad: {pacientes[i][2]} | Diagnóstico: {pacientes[i][3]} | Días: {pacientes[i][4]}")
                encontrado = True

        if encontrado == False:
            print("Paciente no encontrado.")
            seguir = int(input("¿Desea intentar nuevamente? (1: sí / 0: no): "))
        else:
            seguir = 0
