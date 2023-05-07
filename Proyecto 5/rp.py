#Es el Algortimo Extendido de Euclides
def euclides(a, b):
    if b == 0:
        return 0,1,0
    u0 = 1
    u1 = 0
    v0 = 0
    v1 = 1
    while b != 0:
        q = a//b
        r = a - b * q
        u = u0 - q * u1
        v = v0 - q * v1
        #Modificar a,b
        a = b
        b = r
        #Modificaciones para la siguiente iteración
        u0 = u1
        u1 = u
        v0 = v1
        v1 = v
    return  u0

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

    return listaPrimosRelativos

def ordm(a, m, lista_divisores):

    #Definimos la lista para los órdenes posibles
    ordenPosible = []

    for divisor in lista_divisores:

        e = (a**(divisor))%m

        if e == 1:

            ordenPosible.append(divisor)

    o = min(ordenPosible)

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

    #Cuando el número sea válido, llamamos a las funciones respectivas
    lista_primos_relativos = phi(m)
    lista_primos_relativos2 = lista_primos_relativos
    phi_m = len(lista_primos_relativos)
    lista_divisores = divisores(phi_m)
    
    raices_primitivas = []

    while len(raices_primitivas) < 1:
        for primo_relativo in lista_primos_relativos:
            
            orden = ordm(primo_relativo, m, lista_divisores)

            if orden == phi_m:
                raices_primitivas.append(primo_relativo)
                lista_primos_relativos2.remove(primo_relativo)
            else:
                lista_primos_relativos2.remove(primo_relativo)
        break
    
    #Número de raíces primitivas
    if(len(raices_primitivas) == 1):
        
        x0 = euclides(primo_relativo, m)
        #x es el inverso multiplicativo de la raíz primitiva que ya encontramos
        x = x0%m
        phi_phi_m = len(phi(phi_m))
        
    else:
        print(f"{m} no tiene raíces primitivas.")

#Finalmente, llamamos a la funcion inicial del programa, para cuando se ejecute.
elegir()
