#verify.py (nro 2)
import preguntas as p


def verificar(alternativas, eleccion):
    #devuelve el índice de elección dada
    eleccion = ['a', 'b', 'c','d'].index(eleccion)

    # generar lógica para determinar respuestas correctas
    ##########################################################################################
    respuesta_correcta = None
    for alt in alternativas:
        if alt[1] == 1:
            respuesta_correcta = alt[0]
            break

    if respuesta_correcta is None:
            print("Error; no se encontró na la resp correc en las alternt.")
            return False
        

    eleccion_letra = ['a', 'b', 'c', 'd'].index(eleccion)
    respuesta_usuario = alternativas[eleccion_letra][0]
    

    if respuesta_usuario == respuesta_correcta:
         print("Respuesta bien respondida")
         return True
    else:
         print("Respuesta mala")
         return False


    
    
    
    ##########################################################################################
    return correcto



if __name__ == '__main__':
    from print_preguntas import print_pregunta
    
    # Siempre que se escoja la alternativa con alt_2 estará correcta, e incorrecta en cualquier otro caso
    pregunta = p.pool_preguntas['basicas']['pregunta_2']
    print_pregunta(pregunta['enunciado'],pregunta['alternativas'])
    respuesta = input('Escoja la alternativa correcta:\n> ').lower()
    verificar(pregunta['alternativas'], respuesta)






