#Definimos la función para saber si un número es primo
def primo(p):
    #Elevamos a la 0.5 (eso es equivalente a sacar la raíz cuadrada)
    s_p = round(p ** 0.5)
    es_primo = True

    for i in range(2, s_p+1):

        if p%i == 0:

            es_primo = False
    return es_primo

#Definimos la función de Legendre con el método de Euler
def legendre_Euler(a,p):
    #Si a dividide a p, entonces el número de Legendre es 0
    if a%p == 0:
        return 0
    else:
        #Definimos el exponente para hacer la congruencia
        exp = (p-1)//2
        #u será el residuo que se generará de la congruencia
        u = (((a**(exp))-1)%p)
        #Si el residuo es cero, el número de Legendre es 1,
        # de lo contrario, es -1
        if u == 0:
            return 1
        else:
            return -1

#Definimos la función de Legendre con el método de Gauss
def legendre_Gauss(a,p):
    #El número de Legendre por el método de Gauss sólo acepta
    # primos relativos
    if a%p == 0:
        return 0
    else:
        #Tomamos el entero (p-1)/2
        b = (p-1)//2
        #Hacemos la lista de residuos módulo p de los números que
        # van de 1 hasta p-1/2
        lista_residuos = []
        for i in range(1,b+1):
            lista_residuos.append((a*i)%p)

        c = p/2
        #Hacemos la lista de los residuos mayores a p/2
        lista_contada = []
        for i in lista_residuos:
            if c < i:
                lista_contada.append(i)
        #Calculamos la longitud de la lista
        n = len(lista_contada)
        #Por el método de Gauss, (-1)^n es el número de Legendre
        e_2 = (-1)**n
        return e_2

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

        p = int(input("Escribe un primo positivo impar: "))

        if p > 2:
            es_primo = primo(p)
            if es_primo:

                valid_input_2 = True
                print (f"Escogiste el número primo {p}.")
            else:
                print("No escogiste un número primo.")
        else:
            print("No escogiste un primo impar positivo.")

    #Cuando el número sea válido, llamamos a las funciones respectivas
    e_1 = legendre_Euler(a,p)
    e_2 = legendre_Gauss(a,p)

    print(f"El número de Legendre con el método de Euler es {e_1}.")
    print(f"El número de Legendre con el método de Gauss es {e_2}.")

elegir()
