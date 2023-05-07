#Definición de la función phi
def phi(n):
    #Definimos la lista para los primos relativos
    listaPrimosRelativos = []
    #La iteración empezará a partir de 1
    iteracion_numero = 1
    #Todos los números menores o iguales a n cumplirán una función
    while iteracion_numero <= n:
        mcd = algoritmo_div(n,iteracion_numero)
        if mcd == 1:
            listaPrimosRelativos.append(iteracion_numero)
        #Una vez evaluado, pasamos al siguiente número (Le añadimos uno a la variable)    
        iteracion_numero += 1
    numeroPrimosRelativos = len(listaPrimosRelativos)
    #print(f"La función φ({n})={numeroPrimosRelativos}.")
    #Si se desea ver la lista de los primos relativos, quitar el '#' de a continuación
    #print(f"Los elementos de la función φ({n})={listaPrimosRelativos}.")
  
def elegir():
    #Si el usuario no ingresa un número, la app finaliza con un error.
    #'input()' escribe un mensaje en la terminal y recibe el texto que
    # el usuario ingrese.
    #'valid_input' es una variable que determina si el número recibido
    # es un entero positivo (se combina con la función if para la
    # condición '>0')  
    valid_input = False
    while valid_input == False:
        m = int(input("Escribe tu módulo: "))
    if m > 0:
        valid_input = True
        print (f"Escogiste el módulo {m}.")
    else:
        print ("Escogiste un número inválido.")
    valid_input_2 = False
    while valid_input_2 == False:
        a = int(input(f"Escribe tu número al que le sacaremos el orden módulo {m}: "))
    if a > 0:
        valid_input_2 = True
        print (f"Escogiste el número {a}.")
    #Cuando el número sea valido, llama a las funciones respectivas
        #Llamamos 'listaDivisores' a la lista que nos arroja la función
        # divisores, y la insertamos en tau y sigma
    #listaDivisores = divisores(n)
    #tau(n,listaDivisores)
    #sigma(n,listaDivisores)
    #phi(n)
    else:
        print ("Escogiste un número inválido.")
#Finalmente, llamamos a la funcion inicial del programa, para cuando se ejecute.
elegir()
