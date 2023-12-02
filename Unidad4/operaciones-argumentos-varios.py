



#Los argumentos indeterminados
#  "*args" -->  Traducido seria un tupla:   tupla = (3,5,4,4,5)

def  suma(*args):
    resultado = 0.0
    for dato in args:
        resultado += dato
    return  resultado


def  multiplicacion(*args):
    resultado = 1
    for dato in args:
        resultado *= dato
    return  resultado

def  potencia(*args):
    lista  =  []
    for dato in args:
        lista.append(dato**5)
    return  lista


print(f"La suma de los valores enviados es = {suma (2,2,2,2,2,2,2,2,2)}")

print(f"La multiplicacion de los valores enviados es = {multiplicacion (2,2,2,2,2,2,2,2,2)}")

print(f"La potencia de los valores enviados es = {potencia (2,3,4,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2)}")