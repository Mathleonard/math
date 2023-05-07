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
    #Cada uno de los números deberá cumplir la condición, se da que es n/2, ya que
    # se sabe que todo número es divisible por su mitad o alguien menor (si es par
    # o no, respectivamente)

    while iteracion_numero <= n/2:

        #Si el residuo es cero, es porque es divisible por n
        if n%iteracion_numero == 0:
            #'.append()' agrega ese elemento al final de la lista
            listaDivisores.append(iteracion_numero)

        #Manda al siguiente elemento
        iteracion_numero += 1
        #Como un 'else' no afectaría a la lista, no se agrega

    #El mismo número también es un divisor de sí mismo
    listaDivisores.append(n)
    #Regresa la lista de divisores a donde se llamó la función
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

    return o

#Definimos la función que buscará las raíces primitivas
def busca_raiz(raices_primitivas, lista_primos_relativos, phi_phi_m, m, lista_divisores, phi_m):

    #La condición es que ya tenemos la cantidad de las raíces primitivas si es
    # igual a phi(phi(m)) (teorema visto en clase)
    if len(raices_primitivas) == phi_phi_m:

        #Ordena las raíces primitivas de menor a mayor
        raices_primitivas.sort()
        print(f"Las raíces primitivas de {m} son {raices_primitivas}.")

    else:

        #Para cada primo relativo, calculará su orden
        for primo_relativo in lista_primos_relativos:


            orden = ordm(primo_relativo, m, lista_divisores)

            #Si el orden es igual a phi(m), es una raíz primitiva
            if orden == phi_m:

                #Calculamos su inverso multiplicativo (programa del proyecto 3), ya que
                # también será raíz primitiva, al tener el mismo orden
                x0 = euclides(primo_relativo, m)
                i_m = x0%m

                #Añadimos las raíces primitivas a su lista, y las
                # eliminamos de la lista de primos relativos para no contar doble
                raices_primitivas.append(primo_relativo)
                raices_primitivas.append(i_m)
                lista_primos_relativos.remove(primo_relativo)
                lista_primos_relativos.remove(i_m)

                #Vuelve a llamar a la función con las listas modificadas anteriormente
                busca_raiz(raices_primitivas, lista_primos_relativos, phi_phi_m, m, lista_divisores, phi_m)

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

    #Proporcionará la lista de primos relativos a m
    lista_primos_relativos = phi(m)

    #Generará una copia de la lista de primos relativos (no se podrá modificar
    # la lista 1 cuando se use la función 'for...in...')
    lista_primos_relativos2 = lista_primos_relativos

    #Calculamos phi(m) como la cardinalidad de la lista anteriormente creada
    phi_m = len(lista_primos_relativos)

    #Obtenemos los divisores de phi(m)
    lista_divisores = divisores(phi_m)

    #Generamos la lista (vacía, por el momento) de las raíces primitivas
    raices_primitivas = []

    #Asignamos una condición (análogo al valid_input)
    tiene_raices = False

    while not tiene_raices:

        #Buscará una primera raíz primitiva
        for primo_relativo in lista_primos_relativos:

            #Obtiene el orden de cada primo relativo
            orden = ordm(primo_relativo, m, lista_divisores)

            #Si dicho orden es igual a phi(m), entonces es raíz, y el programa sigue
            if orden == phi_m:

                tiene_raices = True

            #Si no tiene el mismo orden, lo eliminará de la lista de primos relativos
            else:

                lista_primos_relativos2.remove(primo_relativo)

        #Ocupamos 'break', para que en caso de que no encuentre raices,
        #aún así salga del ciclo 'while' y el promgrama no se quede atorado aqui.
        break

    #Al encontrar una raíz primitiva, sigue el siguiente código
    if tiene_raices:

        #Calcula phi(phi(m)), ya que es la cantidad de raíces primitivas
        phi_phi_m = len(phi(phi_m))
        #print(f"La cantidad de raíces primitivas es {phi_phi_m}.")
        
        #Llama a la función para obtener todas las raíces primitivas
        busca_raiz(raices_primitivas, lista_primos_relativos2, phi_phi_m, m, lista_divisores, phi_m)

    else:
        #Si no encontró ninguna de las raíces primitivas, en el 'while' pasado, entonces
        # no se sigue ninguna parte del código.
        print(f"{m} no tiene raíces primitivas.")

#Finalmente, llamamos a la funcion inicial del programa, para cuando se ejecute.
elegir()
