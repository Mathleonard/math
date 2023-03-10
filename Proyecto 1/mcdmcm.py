#a y b son los números dados inicialmente
def mcd(a, b, r):
    producto = abs(a*b)
    print(f"El mínimo común múltiplo es {producto//r}.")

#En la primera iteración, 'b' es el número más grande, y 'r' el número más pequeño
def euclides(b, r):
    cociente_e = b//r
    residuo_e = b%r
    print(f"{b}={r}({cociente_e})+{residuo_e}")
    #'!=' significa "no es igual a"
    if residuo_e != 0:
        #se repite el proceso con la pareja (r,residuo_e)
        return euclides(r,residuo_e)

    else:
        print(f"El máximo común divisor es {r}.")
        print("Queda pendiente la combinación lineal")
        #Sale de la función euclides y se regresa a la función de donde se llamó
        return r

#Función inicial: Permite al usuario elegir dos números
def select():
    #Guarda el input() del usuario en las variables "first_number" y "second_number".
    #Si el usuario no ingresa un número, la app finaliza con un error.
    first_number = int(input("Escribe tu primer número: "))
    second_number = int(input("Escribe tu segundo número: "))
    #'f' hace que se puedan poner las variables en el texto con llaves
    print(f"Escogiste la pareja ({first_number}, {second_number}).")
    if first_number<second_number:
        print(f"{first_number} es menor que {second_number}.")
        r = euclides(second_number, first_number)
        mcd(first_number, second_number, r)

    #elif permite tener varias condiciones hasta que se escriba un else
    #(el último caso)
    elif second_number<first_number:
        print(f"{second_number} es menor que {first_number}.")
        r = euclides(second_number, first_number)
        mcd(first_number, second_number, r)

    #El último caso se pone con "else"
    else:
        print(f"{first_number} es igual que {second_number}.")
        r = euclides(second_number, first_number)
        mcd(first_number, second_number, r)


select()
