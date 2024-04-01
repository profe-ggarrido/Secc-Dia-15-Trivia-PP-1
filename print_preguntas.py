#print_preguntas.py (nro 6)
import preguntas as p

def print_pregunta(enunciado, alternativas):
    
    # Imprimir enunciado y alternativas
    ###############################################################
    print(enunciado[0]) # aqui visualizo
    letras = ['A', 'B', 'C', 'D']
    for i, alt in enumerate(alternativas):
        print(f"{letras[i]}.{alt[0]}")  #visualiz de alt con Letras
    
    ###############################################################
        
if __name__ == '__main__':
    # Las preguntas y alternativas deben mostrarse según lo indicado
    pregunta = p.pool_preguntas['basicas']['pregunta_1']
    print_pregunta(pregunta['enunciado'],pregunta['alternativas'])
    
    # Enunciado básico 1

    # A. alt_1
    # B. alt_2
    # C. alt_3
    # D. alt_4