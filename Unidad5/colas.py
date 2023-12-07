
# FIFO (First In First Out).
# deque ---> ([])

from collections import deque

cola_datos = deque()  
                            
cola_datos.appendleft(20)
print(cola_datos)

cola_datos.appendleft(30)
print(cola_datos)

cola_datos.appendleft(40)
print(cola_datos)


print(type(cola_datos))
print(cola_datos)

print("POP")

cola_datos.popleft()
print(cola_datos)

cola_datos.popleft()
print(cola_datos)

cola_datos.popleft()
print(cola_datos)

