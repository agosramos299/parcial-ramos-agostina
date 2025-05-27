def ordenar_por_historia(pacientes: list[list]):
    """
    Ordena la lista de pacientes por número de historia clínica utilizando el método Bubble Sort.

    Después de ordenar, se pregunta al usuario si desea ver la lista ordenada y,
    en caso afirmativo, imprime cada paciente con sus datos formateados.

    Args:
        pacientes (list[list]): Lista de pacientes, donde cada paciente es una lista
                                con los siguientes datos en orden:
                                [historia_clínica, nombre, edad, diagnóstico, días_internado]
    """


    for i in range(len(pacientes)):
        for j in range(0, len(pacientes) - i - 1):
            if pacientes[j][0] > pacientes[j + 1][0]:
                aux = pacientes[j]
                pacientes[j] = pacientes[j + 1]
                pacientes[j + 1] = aux

    print("Pacientes ordenados por número de historia clínica.")

    mostrar = input("¿Desea ver la lista ordenada? (s: sí / n: no): ")

    if mostrar == "s":
        for i in range(len(pacientes)):
            print(f"Historia: {pacientes[i][0]} | Nombre: {pacientes[i][1]} | Edad: {pacientes[i][2]} | Diagnóstico: {pacientes[i][3]} | Días: {pacientes[i][4]}")
    else:
        print("Lista no mostrada.")

