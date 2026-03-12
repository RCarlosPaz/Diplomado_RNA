#Función para contar caracteres en una cadena

print("\n1. Función para contar caracteres de una cadena\n")

def contar_caracteres(caracteres):
    contador = len(caracteres)
    print("La frase '",caracteres,"' tiene",contador,"caracteres\n", sep=" ")
    
caracteres = 'Aprender Python es divertido'
contar_caracteres(caracteres)


#Función para convertir y mostrar tipos de números

print("\n2. Función para convertir y mostrar tipos de números\n")

def convertir_numero(num):
    entero = num
    cadena = str(num)
    flotante = float(num) 
    print(f'1. Entero: {entero}, Tipo: ',type(entero)) 
    print(f'2. Cadena: {cadena}, Tipo: ',type(cadena)) 
    print(f'3. Flotante: {flotante}, Tipo: {type(flotante)}\n') 
    num = int
convertir_numero(42)

