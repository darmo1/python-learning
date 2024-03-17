#listas
rango = list(range(1,11))

numeros = [1,2,3,4,5,6,7,8,9]
primero, segundo, tercero, *demas = numeros

#tambien puedo agrupar asi
numbers = [1,2,3,4,5,6,7,8,9]
primero, segundo, *otros,      ultimo = numbers
# 1        2     [3,4,5,6,7,8] , 9 


mascotas = ['pelusa', 'pulga', 'felipe', 'chanchito feliz']
for mascotas in enumerate(mascotas):
    print(mascota)

    #this return a tupla [(0, 'pelusa), (1, pulga) ......]


if('pelusa' in mascotas):
    print(mascotas.index('pelusa'))

##INSERTAR EN UN ESPECIFICO INDEX
mascotas.insert(1, 'Melvin') #insert in the specific index
mascotas.insert(-1, 'Melvin') # insert in the last position
mascotas.append('Melvin 2') # -> insert at the end of the list

##REMOVE
mascotas.remove('Pulga')
mascotas.pop() #remove the last element in the list
mascostas.pop(1) # remove the eement in the specific index
del mascotas[0] # It is deleting the element in this specific index
mascotas.clear() #delete all elements in the list

#Sort the list
#sorted crea una copia de la lista
numerosSorted = sorted(numeros)
#reverseSorted = numeros.sort(reverse=True)
