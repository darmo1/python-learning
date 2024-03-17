#FILAS - FIRST IN FIRST OUT = FIFO
lista = list(1,2,3,4)

from collections import deque

fila = deque([1,2])
fila.append(3)
fila.append(4)
fila.append(5)

fila.popleft()




#PILAS -> LIFO LAST IN FIRST OUT