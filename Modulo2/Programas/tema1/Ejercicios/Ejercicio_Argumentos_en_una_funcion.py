print("La fiesta de cumpleaños de Python\n")

tema = "Python"
lugar = "aula de informatica"

def organizar_fiesta(arg,arg2=tema,arg3=lugar):
    print(f'Preparando una fiesta para {arg} invitados\n')
    print(f'Tema de la fiesta: {arg2}\n')
    print(f'Lugar de la celebración: {arg3}\n')
    

#def organizar_fiesta(arg,arg2="Python", arg3 ="aula de informatica"):
  
   # print(f'Preparando una fiesta para {arg} invitados\n')
    #print(f'Tema de la fiesta: {arg2}\n')
   # print(f'Lugar de la celebración: {arg3}\n')


organizar_fiesta(25)
#organizar_fiesta(25,"Python")
#organizar_fiesta(25,"Python","aula de informatica")

