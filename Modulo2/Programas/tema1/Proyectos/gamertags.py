def cabecera():
    """Muestra la cabecera de la aplicación"""
    titulo = r"""
 $$$$$$\                                           $$$$$$$$\                            
$$  __$$\                                          \__$$  __|                           
$$ /  \__| $$$$$$\  $$$$$$\$$$$\   $$$$$$\   $$$$$$\  $$ | $$$$$$\   $$$$$$\   $$$$$$$\ 
$$ |$$$$\  \____$$\ $$  _$$  _$$\ $$  __$$\ $$  __$$\ $$ | \____$$\ $$  __$$\ $$  _____|
$$ |\_$$ | $$$$$$$ |$$ / $$ / $$ |$$$$$$$$ |$$ |  \__|$$ | $$$$$$$ |$$ /  $$ |\$$$$$$\  
$$ |  $$ |$$  __$$ |$$ | $$ | $$ |$$   ____|$$ |      $$ |$$  __$$ |$$ |  $$ | \____$$\ 
\$$$$$$  |\$$$$$$$ |$$ | $$ | $$ |\$$$$$$$\ $$ |      $$ |\$$$$$$$ |\$$$$$$$ |$$$$$$$  |
 \______/  \_______|\__| \__| \__| \_______|\__|      \__| \_______| \____$$ |\_______/ 
                                                                    $$\   $$ |          
                                                                    \$$$$$$  |          
                                                                     \______/           
       🎮 ¡Crea tu identidad gamer! 🎮                              
"""
    print(titulo)

#cabecera()

def crear_tag_basico(nombre):
    """
    Crea un gamer tag basico usando las primeras 4 letras del nombre.

    Parametro:
    nombre(str): El nombre del usuario

    Retorna:
    str: Gamertag basico
    """
    tag = nombre[0:4]
    return tag
   
#tag_basico = crear_tag_basico("Roberto")
#print(tag_basico)
    
def crear_tag_invertido(nombre):
    """
    CRea un gamertag invirtiendo el nombre completo

    Parametro:
    str: El nombre del usuario

    Retorna:
    str: Gamertag invertido
    """
    tag = nombre[::-1]
    return tag
#tag_invertido = crear_tag_invertido("Roberto")
#print(tag_invertido)


def crear_tag_intercalado(nombre,apellido):
    """
    Crea un gamertag intercalado combinando las iniciales del nombre y apellido, seguidas del resto de cada uno


    Parametros:

    str: El nombre del usuario

    str: El apellido del usuario

    Retorna:

    str: Gamertag intercalado
    """
    Inicialnombre = nombre[0]
    inicialapellido = apellido [0]

    print(f'\n3. TAG INTERCALADO: {Inicialnombre}{inicialapellido}{nombre[1:]}{apellido[1:]}',sep="")    
    
def crear_tag_elite(nombre):
    """
    Crea un gamertag combinando las primeras dos letras del nombre con las ultimas dos letras.

    Parametros:

    str: nombre del usuario

    Retorna:

    None (imprime directamente)
    """
    inicionombre = nombre[:2]
    finNombre = nombre[-2:]
    print("\n4. TAG ELITE: ", inicionombre, finNombre, sep="")

def crear_tag_con_numero(nombre, numero):
    """
    Crea un gamertag agregando numero favorito despues de las primeras 5 letras del nombre

    Parametros:
    str: nombre del usuario
    str: numero favorito del usuario

    Retorna:

    None (Imprime directamente)
    """
    print("\n5. TAG CON NUMERO: ", nombre[:5],numero, sep="")


def mostrar_estadisticas(nombre):
    """
    Muestra estadisticas del nombre proporcionado.

    Parametro:

    nombre(str): El nombre a analizar

    Retorno:

    None (Imprime directamente)
    """
    longitud_nombre = len(nombre)
    print("\n 📊 Estadisticas de tu nombre:")
    print("Nombre completo:", nombre)
    print("Longitud del nombre:", longitud_nombre)
    print("Primera letra:", nombre[0])
    print("Ultima letra:", nombre[-1])

def generar_todas_opciones(nombre, apellido, numero):
    """
    Genera y muestra todas las opciones de Gamertags

    Parametros:
    nombre (str): Nombre del usuario
    apellido (str): Apellido del usuario
    numero (str): Numero favorito del usuario

    Retorna:
    None (Imprime directamente)
    """
    print("\n========================================================")
    print(" 🎯 TUS OPCIONES DE GAMERTAG:")
    print("========================================================")

    tag_basico = crear_tag_basico(nombre)
    print("\n1. TAG BASICO", tag_basico)
    print("\n2. TAG INVERTIDO: ", crear_tag_invertido(nombre))
    crear_tag_intercalado(nombre,apellido)
    crear_tag_elite(nombre)
    crear_tag_con_numero(nombre, numero)


    print("========================================================")



# ==================================================================================
# APLICACION PRINCIPAL
# ==================================================================================
# llamar a la función cabecera
cabecera()

#Solicitar datos al usuario
nombre = input("\nIntroduce tu nombre: ")
apellido = input("\nIntroduce tu apellido: ")
numero = input("\nIntroduce tu numero favorito: ")

# Mostrar estadisticas del nombre
mostrar_estadisticas(nombre)
generar_todas_opciones(nombre, apellido, numero)


print("\n 🌟¡Elige tu favorito y conquista el mundo gamer!🌟\n")

