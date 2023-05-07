#Definición de la función divisores
def divisores(n):
    #Se crea la lista vacía de divisores
    listaDivisores = []
    #Asignamos la iteración a partir de 1
    iteracion_numero = 1
    #Cada uno de los números deberá cumplir la condición
    while iteracion_numero <= n/2:
        if n%iteracion_numero == 0:
            #'.append()' agrega ese elemento al final de la lista
            listaDivisores.append(iteracion_numero)
        iteracion_numero += 1
        #Como un 'else' no afectaría a la lista, no se agrega
    #print(f"Sus divisores son {listaDivisores}.")
    #Regresa la lista de divisores a donde se llamo la función
    listaDivisores.append(n)
    return listaDivisores

def algoritmo_div(n, a):

    #Cuando nada más hay un '=', el programa guarda el valor del lado derecho
    # a las variables del lado izquierdo.
    #El uso de '%' es para obtener el residuo del cociente: el módulo

    residuo_ad = n%a

    #'f' permite ingresar variables dentro de un texto común (string)
    #Las variables se ponen entre llaves, cuando estamos en texto común

    #La función 'if' empieza como un 'si (condición)'
    #'!=' significa 'no es igual a'
    if residuo_ad != 0:
        return algoritmo_div(a,residuo_ad)

    #'else' es el último caso del condicional, y se usa cuando no se cumple

    else:
        s = abs(a)
        #'return <>' regresa el valor a donde fue llamada la función
        return s

#Definición de la función phi
def phi(m):

    #Definimos la lista para los primos relativos
    listaPrimosRelativos = []

    #La iteración empezará a partir de 1
    iteracion_numero = 1

    #Todos los números menores o iguales a m cumplirán una función
    while iteracion_numero <= m:

        mcd = algoritmo_div(m,iteracion_numero)

        if mcd == 1:

            listaPrimosRelativos.append(iteracion_numero)
        #Una vez evaluado, pasamos al siguiente número (Le añadimos uno a la variable)    

        iteracion_numero += 1

    numeroPrimosRelativos = len(listaPrimosRelativos)

    return numeroPrimosRelativos

def ordm(a, m, lista_divisores):

    #Definimos la lista para los órdenes posibles
    ordenPosible = []

    #Buscamos para cada uno de los elementos de la lista
    for divisor in lista_divisores:


    #Calculamos el módulo de a^n para cada n divisor
        e = (a**(divisor))%m

    #Buscamos que e sea congruente a 1 módulo m
        if e == 1:
        
        #Añadimos el divisor a la lista de órdenes candidatos
            ordenPosible.append(divisor)

    #Al finalizar el proceso, se indica a "o" como el mínimo "e"
    o = min(ordenPosible)

    #Devolvemos el valor de "o"
    return o

def elegir():

    #Si el usuario no ingresa un número, la app finaliza con un error.
    #'input()' escribe un mensaje en la terminal y recibe el texto que
    # el usuario ingrese.
    #'valid_input' es una variable que determina si el número recibido
    # es un entero positivo (se combina con la función if para la
    # condición '>0')  
    valid_input = False

    while not valid_input:

        m = int(input("Escribe tu módulo: "))

        if m > 0:

            valid_input = True
            print (f"Escogiste el módulo {m}.")

        else:

            print ("Escogiste un número inválido.")

    #Elegimos una segunda condición, ya que también debe ser un entero positivo
    valid_input_2 = False

    while not valid_input_2:

        a = int(input(f"Escribe tu número al que le sacaremos el orden módulo {m}: "))

        if a > 0:

            valid_input_2 = True
            print (f"Escogiste el número {a}.")

        else:

            print ("Escogiste un número inválido.")

    #Cuando los números sean válidos, llamamos a las funciones respectivas
    #Llamamos a la función phi(m) para calcular el número de primos relativos
    phi_m = phi(m)
    
    #Llamamos a la función divisores para saber cuáles son los posibles candidatos
    # a ser los órdenes de m
    lista_divisores = divisores(phi_m)
    
    #Llamamos a la función orden para saber cuál es el mínimo de todos los candidatos
    o = ordm(a, m, lista_divisores)
    print(f"El orden de {a} módulo {m} es {o}.")

#Finalmente, llamamos a la funcion inicial del programa, para cuando se ejecute.
elegir()
