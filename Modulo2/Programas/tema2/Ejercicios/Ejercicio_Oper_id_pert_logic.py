#Juego de adivinanza con letras y palabras
palabra_adivinar = "Diplomado"

def adivinar_palabra(letra_prueba, palabra_intento):
    """
    Utilizar operadores de pertenencia, comparación y logicos.
    Parametros:

    letra_prueba: (str)

    palabra_intento: (str)

    Retorna:

    letra_en_palabra: (bool)
    """
    # Verificar Letra en Palabra
    #Utlizando operadores de pertenencia: (in y not int)
    
    letra_en_palabra = letra_prueba in palabra_adivinar

    print(f'¿La letra de prueba se encuentra en la palabra? {letra_en_palabra}\n')

    #Adivinar la palabra
    #Utilizando operadores de comparación (==,!=,<,<=,>,>=)

    resultado_comparación = palabra_intento == palabra_adivinar

    #Utilizando operadores logicos (not, or y and)

    resultado_adivinanza = len(palabra_intento) == len(palabra_adivinar)

    print(f'El jugador gana: {resultado_adivinanza}')


adivinar_palabra("o","Diplomado")