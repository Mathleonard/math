#Definición de la función divisores
def divisores(n):
    #Se crea la lista vacía de divisores
    listaDivisores = []
    #Asignamos la iteración a partir de 1
    iteracion_numero = 1
    #Cada uno de los números deberá cumplir la condición
    while iteracion_numero <= n:
        if n%iteracion_numero == 0:
            #'.append()' agrega ese elemento al final de la lista
            listaDivisores.append(iteracion_numero)
        iteracion_numero += 1
        #Como un 'else' no afectaría a la lista, no se agrega
    print(f"Sus divisores son {listaDivisores}.")
    #Regresa la lista de divisores a donde se llamo la función
    return listaDivisores
#Definición de la función tau
def tau(n,listaDivisores):
    #Asignamos la variable para contar los divisores
    #'.lenght' dará la cantidad de elementos que tiene la lista
    numeroDivisores = len(listaDivisores)
    print(f"La función τ({n})={numeroDivisores}.")
#Definición de la función sigma
def sigma(n,listaDivisores):
    #Definimos la variable 'sumaDivisores' como 0 (primer elemento)
    sumaDivisores = 0
    #Cada elemento de la lista se sumará a 'sumaDivisores'
    for elemento in listaDivisores:
        #'+=' es lo mismo que 'sumaDivisores=sumaDivisores+elemento'
        sumaDivisores += elemento
    print(f"La función σ({n})={sumaDivisores}.")

#La función 'algoritmo_div()' regresará el mcd de 2 números.
#Además, guardará el procedimiento realizado en una lista/arreglo.
def algoritmo_div(n, a):
    #Cuando nada más hay un '=', el programa guarda el valor del lado derecho
    # a las variables del lado izquierdo.
    #El uso de '//' es para obtener el cociente redondeado hacia abajo
    cociente_ad = n//a
    #El uso de '%' es para obtener el residuo del cociente: el módulo
    residuo_ad = n%a
    #'f' permite ingresar variables dentro de un texto común (string)
    #Las variables se ponen entre llaves, cuando estamos en texto común
    procedimiento_txt = (f"{n}={a}({cociente_ad})+({residuo_ad})")

    #La función 'if' empieza como un 'si (condición)'
    #'!=' significa 'no es igual a'
    if residuo_ad != 0:
        return algoritmo_div(a,residuo_ad)

    #'else' es el último caso del condicional, y se usa cuando no se cumple
    # el 'if
    else:
        s = abs(a)
        #'return <>' regresa el valor a donde fue llamada la función
        return s

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
    print(f"La función φ({n})={numeroPrimosRelativos}.")
    #Si se desea ver la lista de los primos relativos, quitar el '#' de a continuación
    print(f"Los elementos de la función φ({n})={listaPrimosRelativos}.")
    
def elegir():
    #Si el usuario no ingresa un número, la app finaliza con un error.
    #'input()' escribe un mensaje en la terminal y recibe el texto que
    # el usuario ingrese.
    #'valid_input' es una variable que determina si el número recibido
    # es un entero positivo (se combina con la función if para la
    # condición '>0')
    valid_input = False
    while valid_input == False:
        n = int(input("Escribe tu número: "))
        if n > 0:
            valid_input = True
            print (f"Escogiste el número {n}.")
            #Cuando el número sea valido, llama a las funciones respectivas
            #Llamamos 'listaDivisores' a la lista que nos arroja la función
            # divisores, y la insertamos en tau y sigma
            listaDivisores = divisores(n)
            tau(n,listaDivisores)
            sigma(n,listaDivisores)
            phi(n)
        else:
            print ("Escogiste un número inválido.")
#Finalmente, llamamos a la funcion inicial del programa, para cuando se ejecute.
elegir()
