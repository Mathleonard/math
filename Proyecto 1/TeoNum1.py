#'def' lo usamos para definir funciones
#La función 'algoritmo_div()' regresará el mcd de 2 números.
#Además, guardará el procedimiento realizado en una lista/arreglo.
def algoritmo_div(b, r, lista):
    #Cuando nada más hay un '=', el programa guarda el valor del lado derecho
    # a las variables del lado izquierdo.
    #El uso de '//' es para obtener el cociente redondeado hacia abajo
    cociente_ad = b//r
    #El uso de '%' es para obtener el residuo del cociente: el módulo
    residuo_ad = b%r
    #'f' permite ingresar variables dentro de un texto común (string)
    #Las variables se ponen entre llaves, cuando estamos en texto común
    procedimiento_txt = (f"{b}={r}({cociente_ad})+({residuo_ad})")
    #'append()' permite ingresar un valor (variable, texto o número) en la
    #siguiente posición disponible en una lista/arreglo.
    lista.append(procedimiento_txt)
    #'print()' muestra un texto en la terminal
    print(procedimiento_txt)

    #La función 'if' empieza como un 'si (condición)'
    #'!=' significa 'no es igual a'
    if residuo_ad != 0:
        return algoritmo_div(r,residuo_ad, lista)

    #'else' es el último caso del condicional, y se usa cuando no se cumple
    # el 'if
    else:
        s = abs(r)
        print(f"El máximo común divisor es {s}.")
        #'return <>' regresa el valor a donde fue llamada la función
        return s

#La función 'mcm()' regresará el mcm de 2 números.
def mcm(a, b, r):
    m = abs(a*b)//r
    print(f"El mínimo común múltiplo es {m}.")
    return m

#La función 'algoritmo_euclides()' está en progreso.
#Actualmente, solo recorre la lista/arreglo del procedimiento obtenido en
#la función algoritmo_div()
#Debemos hacer que separe el procedimiento para que lo muestre 'invertido'
#despejando el número más a la derecha de la ecuación
def algoritmo_euclides(lista):
    lista2 = []
    for i in range(len(lista)):
        tmp = lista[i].split("=")
        for j in range(len(tmp)):
            print(tmp[j])

#La función 'elegir()' permite al usuario ingresar 2 números.
#Estos números servirán para desarrollar la actividad.
def elegir():
    #Si el usuario no ingresa un número, la app finaliza con un error.
    #'int()' indica que lo que prcede se convertirá a un número.
    #'input()' escribe un mensaje en la terminal y recibe el texto que
    # el usuario ingrese.
    number_a = int(input("Escribe tu primer número: "))
    number_b = int(input("Escribe tu segundo número: "))
    print(f"Escogiste la pareja ({number_a}, {number_b}).")
    #Se puede crear y asignar una lista a una variable usando '<nombre_lista> = []'
    lista_procedimiento = []
    
    if number_a<number_b:
        print(f"{number_a} es menor que {number_b}, es decir, {number_a}<{number_b}")
        #La variable 'mcd' llama a la función algoritmo_div y almacena el valor que regresa.
        mcd = algoritmo_div(number_b, number_a, lista_procedimiento)
        print(f"Es decir, mcd({number_a},{number_b})={mcd}.")
        m = mcm(number_a, number_b, mcd)
        print (f"Es decir, mcm({number_a},{number_b})={m}.")
        algoritmo_euclides(lista_procedimiento)

    #La función 'elif' es la siguiente conficional, por si no se cumplió 'if',
    # pero no es la última condición.
    elif number_b<number_a:
        print(f"{number_b} es menor que {number_a}, es decir, {number_b}<{number_a}.")
        mcd = algoritmo_div(number_a, number_b, lista_procedimiento)
        print(f"Es decir, mcd({number_a},{number_b})={mcd}.")
        m = mcm(number_a, number_b, mcd)
        print (f"Es decir, mcm({number_a},{number_b})={m}.")
        algoritmo_euclides(lista_procedimiento)

    else:
        print(f"{number_a} es igual que {number_b}, es decir, {number_a}={number_b}.")
        if number_a>0:
            mcd = algoritmo_div(number_a, number_b, lista_procedimiento)
            print(f"Es decir, mcd({number_a},{number_b})={mcd}.")
            m = mcm(number_a, number_b, mcd)
            print (f"Es decir, mcm({number_a},{number_b})={m}.")
            print (f"La combinación lineal es {number_a}(1)+{number_b}(0)={mcd}")

        elif number_a==0:
            print("0=0(w)+0, con w en los enteros.")
            print("El máximo común divisor es w, con w en los enteros sin el 0.")
            print("Es decir, mcm(0,0)=w, con w en los enteros sin el 0.")
            print("El mínimo común múltiplo es 0.")
            print("Es decir, mcm(0,0)=0.")
            print("La combinación lineal es 0(w_1)+0(w_2)=0, con w_1 y w_2 en los enteros.")

        else:
            mcd = algoritmo_div(number_a, number_b, lista_procedimiento)
            print(f"Es decir, mcd({number_a},{number_b})={mcd}.")
            m = mcm(number_a, number_b, mcd)
            print (f"Es decir, mcm({number_a},{number_b})={m}.")
            print (f"La combinación lineal es {number_a}(-1){number_b}(0)={mcd}")

#Finalmente, llamamos a la funcion inicial del programa, para cuando se ejecute.
elegir()
