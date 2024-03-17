#{ string: any value }

punto = { "x" : 25 , "y": 50 } 

print(punto(['x']), punto.get('x'))

#tambien puedes agregar una propiedad asi punto.get('key', 'value')

for valor in punto:
    print( valor, punto[valor])

for llave, valor in punto.items():
    print(llave, valor)


#OPERADOR DE DESEMPAQUETAMIENTO  *
lista = [1, 2, 3,4]
print(*lista)
    

#para hacer spread en obj
punto1={'x': 19}
punto2={'y': 15}

nuevo_punto = { **punto1, **punto2 }  # DOBLE ASTERISCO