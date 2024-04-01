def verificar(alternativas, eleccion):
    # Validar que la elección sea válida
    eleccion_valida = eleccion in ['a', 'b', 'c', 'd']
    if not eleccion_valida:
        print("Elección inválida. Ingrese 'a', 'b', 'c' o 'd'.")
        return False

    # Obtener el índice de la elección del usuario
    letras = ['a', 'b', 'c', 'd']
    eleccion_indice = letras.index(eleccion)

    # Generar lógica para determinar respuestas correctas
    respuesta_correcta = None
    for alt in alternativas:
        if alt[1] == 1:
            respuesta_correcta = alt[0]
            break

    if respuesta_correcta is None:
        print("Error; no se encontró ninguna respuesta correcta en las alternativas.")
        return False

    respuesta_usuario = alternativas[eleccion_indice][0]
    if respuesta_usuario == respuesta_correcta:
        print("Respuesta bien respondida")
        return True
    else:
        print("Respuesta mala")
        return False