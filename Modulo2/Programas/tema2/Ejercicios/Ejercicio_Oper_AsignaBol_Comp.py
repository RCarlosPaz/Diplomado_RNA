#Asignacion, booleanos y comparación
print("\nComparador de Longitudes de Palabras\n")
palabra1 = "gato"
palabra2 = "perro"
def comparar_longitud(palabra1,palabra2):
    """
    Funcion que compara la longitud de palabras

    Parametros:

    palabra1 (str): cadena de texto 1 

    palabra2 (str): cadena de texto 2
    
    Retorna:

    booleano resultante
    """
    longitud1= len(palabra1)
    longitud2 = len(palabra2)

    comparacion = longitud1 == longitud2

    return comparacion
comparacion = comparar_longitud(palabra1,palabra2)
print(f'¿Son "{palabra1}" y "{palabra2}" dos palabras con la misma longitud? {comparacion}\n')
