def pedir_entero(mensaje: str, minimo: int = None, permitir_cero: bool = True) -> int:
    """
    Solicita al usuario un número entero válido y lo retorna.

    Parámetros:
        mensaje (str): Texto que se muestra al usuario.
        minimo (int, opcional): Valor mínimo permitido. Si es None, no se valida mínimo.
        permitir_cero (bool): Si es False, no se permite ingresar 0.

    Retorna:
        int: El número validado ingresado por el usuario.
    """
    entrada = input(mensaje)

    while entrada.isdigit() == False or (
        permitir_cero == False and int(entrada) == 0
    ):
        print("Entrada inválida. Intente nuevamente.")
        entrada = input(mensaje)

    return int(entrada)

