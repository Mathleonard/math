#Definimos la función para saber si un número es primo
def primo(p):
    s_p = 

def elegir():

    #Si el usuario no ingresa un número, la app finaliza con un error.
    #'input()' escribe un mensaje en la terminal y recibe el texto que
    # el usuario ingrese.
    #'valid_input' es una variable que determina si el número recibido
    # es un entero positivo (se combina con la función if para la
    # condición '>0')
    valid_input = False

    while not valid_input:

        a = int(input("Escribe un número entero positivo: "))

        if a > 0:

            valid_input = True
            print (f"Escogiste el número {a}.")

        else:

            print ("Escogiste un número inválido.")
    
    #Elegimos una segunda condición, ya que también debe ser un entero entre 1 y m
    valid_input_2 = False

    while not valid_input_2:

        p = int(input("Escribe un número primo positivo impar: "))

        if :

            valid_input_2 = True
            print (f"Escogiste el número primo {a}.")

        else:

            print ("No escogiste un número primo.")
    
    #Cuando el número sea válido, llamamos a las funciones respectivas
    
elegir()