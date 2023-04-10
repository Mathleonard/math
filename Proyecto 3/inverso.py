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
def phi(m):
    #Definimos la lista para los primos relativos
    listaPrimosRelativos = []
    #La iteración empezará a partir de 1
    iteracion_numero = 1
    #Todos los números menores o iguales a n cumplirán una función
    while iteracion_numero <= m:
        mcd = algoritmo_div(m,iteracion_numero)
        if mcd == 1:
            listaPrimosRelativos.append(iteracion_numero)
        #Una vez evaluado, pasamos al siguiente número (Le añadimos uno a la variable)    
        iteracion_numero += 1

#La función 'elegir()' permite al usuario ingresar 2 números.
#Estos números servirán para desarrollar la actividad.
def elegir():
    #Si el usuario no ingresa un número, la app finaliza con un error.
    #'int()' indica que lo que procede se convertirá a un número.
    #'input()' escribe un mensaje en la terminal y recibe el texto que
    # el usuario ingrese.
        #'valid_input' es una variable que determina si el número recibido
    # es un entero positivo (se combina con la función if para la
    # condición '>0')
    positivo = False
    while positivo == False:
        m = int(input("Escribe el módulo: "))
        if m > 1:
            positivo = True
            phi(m)
        else:
            print ("Escogiste un número inválido.")     

    
elegir()