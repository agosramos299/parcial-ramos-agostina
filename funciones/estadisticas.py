def paciente_mas_dias(pacientes: list) -> list:
    """
    Imprime en consola el paciente que tiene la mayor cantidad de días de internación.

    Args:
        pacientes (list[list]): Lista de pacientes.

    """
    maximo = pacientes[0][4]
    indice = 0
    for i in range(1, len(pacientes)):
        if pacientes[i][4] > maximo:
            maximo = pacientes[i][4]
            indice = i
    print("Paciente con más días de internación:")
    print(pacientes[indice])

def paciente_menos_dias(pacientes: list):
    """
    Imprime en consola el paciente que tiene la menor cantidad de días de internación

    Args:
        pacientes (list): lista de pacientes

    """
    minimo = pacientes[0][4]
    indice = 0
    for i in range(1, len(pacientes)):
        if pacientes[i][4] < minimo:
            minimo = pacientes[i][4]
            indice = i
    print("Paciente con menos días de internación:")
    print(pacientes[indice])

def contar_mas_de_5_dias(pacientes: list):
    """
    Cuenta e imprime la cantidad de pacientes que han estado internados más de 5 días.

    Args:
        pacientes (list): lista de pacientes

    """
    contador = 0
    for paciente in pacientes:
        if paciente[4] > 5:
            contador += 1
    print(f"Cantidad de pacientes con más de 5 días de internación: {contador}")

def promedio_dias(pacientes: list):
    """
    Calcula e imprime el promedio de días de internación de todos los pacientes registrados.

    Args:
        pacientes (list): lista de pacientes

    """
    suma = 0
    for paciente in pacientes:
        suma += paciente[4]
    promedio = suma / len(pacientes)
    print(f"Promedio de días de internación: {promedio}")
