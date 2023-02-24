#'def' lo usamos para definir funciones
def algoritmo_div(b, r):
    #Cuando nada más hay un '=', el programa guarda el valor del lado derecho
    # a las variables del lado izquierdo.
    #El uso de '//' es para obtener el cociente redondeado hacia abajo
    cociente_ad = b//r
    #El uso de '%' es para obtener el residuo del cociente: el módulo
    residuo_ad = b%r
    #'print' muestra un texto en la aplicación
    #'f' permite ingresar variables dentro de un texto común (string)
    #Las variables se ponen entre llaves, cuando estamos en texto común
    print(f"{b}={r}({cociente_ad})+({residuo_ad})")

    #La función 'if' empieza como un 'si (condición)'
    #'!=' significa 'no es igual a'
    if residuo_ad != 0:
        return algoritmo_div(r,residuo_ad)

    #'else' es el último caso del condicional, y se usa cuando no se cumple
    # el 'if

    else:
        s = abs(r)
        print(f"El máximo común divisor es {s}.")
        #'return' regresa el valor a donde fue llamada la función
        return s

def mcm(a, b, r):
    m = abs(a*b)//r
    print(f"El mínimo común múltiplo es {m}.")
    return m

def elegir():
    #Si el usuario no ingresa un número, la app finaliza con un error.
    #'int()' indica que lo que prcede se convertirá a un número.
    #'input()' escribe un mensaje en la terminal y recibe el texto que
    # el usuario ingrese.
    number_a = int(input("Escribe tu primer número: "))
    number_b = int(input("Escribe tu segundo número: "))
    print(f"Escogiste la pareja ({number_a}, {number_b}).")

    if number_a<number_b:
        print(f"{number_a} es menor que {number_b}, es decir, {number_a}<{number_b}")
        #La variable 'mcd' llama a la función algoritmo_div y almacena el valor que regresa.
        mcd = algoritmo_div(number_b, number_a)
        print(f"Es decir, mcd({number_a},{number_b})={mcd}.")
        m = mcm(number_a, number_b, mcd)
        print (f"Es decir, mcm({number_a},{number_b})={m}.")

    #La función 'elif' es la siguiente conficional, por si no se cumplió 'if',
    # pero no es la última condición.
    elif number_b<number_a:
        print(f"{number_b} es menor que {number_a}, es decir, {number_b}<{number_a}.")
        mcd = algoritmo_div(number_a, number_b)
        print(f"Es decir, mcd({number_a},{number_b})={mcd}.")
        m = mcm(number_a, number_b, mcd)
        print (f"Es decir, mcm({number_a},{number_b})={m}.")

    else:
        print(f"{number_a} es igual que {number_b}, es decir, {number_a}={number_b}.")
        if number_a>0:
            mcd = algoritmo_div(number_a, number_b)
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
            mcd = algoritmo_div(number_a, number_b)
            print(f"Es decir, mcd({number_a},{number_b})={mcd}.")
            m = mcm(number_a, number_b, mcd)
            print (f"Es decir, mcm({number_a},{number_b})={m}.")
            print (f"La combinación lineal es {number_a}(-1){number_b}(0)={mcd}")

#Finalmente, llamamos a la funcion inicial del programa, para cuando se ejecute.
elegir()
