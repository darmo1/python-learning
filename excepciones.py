try:
    n2 = int(input('ingresa primero numero'))
except:
    print('ocurrio un error')

'''tipos de excepciones
   Exception as e
    Tenemos errores como NameError, 
    Es decir el tipo de error depende el codigo que estamos ejecutando

'''

try:
    n2 = int(input('ingresa primero numero'))
except Exception as e:
    print('ocurrio un error')

try:
    n2 = int(input('ingresa primero numero'))
except ValueError as e:
    print('ocurrio un error')
else:
    print('no ocurrio ningun error')
finally:
    print('la ultima ejecucion')


def divison(n=0):
    if n== 0:
        raise Exception('no se puede dividir por cero', f'{n}')
    

try:
    division()
except ZeroDivisionError as e:
    print(e)