import random
import pprint

autos = []  #Guarda los autos ingresados, no sé bien como usarlo como un array de numpy.


#Funciones menores
def verificar_patente(patente):
     return 6 >= len(patente) #Queria intentar verificar que fueran 4 letras y 2 números, encontre una forma con expresiónes regulares pero no entendí demasiado.

def verificar_marca(marca):
    return 5 <= len(marca) <= 12 #Hice estas tres funciones para entenderme un poco más, creo que dividiré el codigo en una función por archivo

def verificar_precio(precio): #Vericia precio
    if precio >= 500000:
        return True

def mostrar_certificados(): #Muestra los certificados
    return

#Funciones mayores
def grabar_vehiculo():
    while True:
        auto = { #Diccionario para guardar los autos
            'Tipo' : input('Ingrese el tipo de auto: '),
            'Patente': '',
            'Marca': '',
            'Precio': '',
            'Multas': {
                'Fecha' : [],
                'Monto' : [],
            },
            'Fecha registro': input('Ingrese la fecha de registro: '),
            'Dueño' : {
                'Nombre' : input('Ingrese el nombre del dueño del auto: '),
                'Apellido' : input('Ingrese el apellido paterno del dueño del auto: '),
                'RUN' : ''
            }
            }
        
        while True:
            run = input('Ingresar rut del dueño (Sin puntos ni guión): ')
            if len(run) >= 8: #Verifica si el rut es igual o mayor a 8 digitos, si es así normaliza el guión (Sacado del ejercicio de array)
                run = run[:-1] + "-" + run[-1]
                auto['Dueño']['RUN'] = run
                break
            else:
                print('Datos invalidos')
                continue
        
        while True: #ingreso de patente
            patente = input('Ingrese la patente del vehiculo: ')
            patente = patente.upper()
            if verificar_patente(patente) == True:
                auto['Patente'] = patente
                break
            else:
                print('Datos no validos, reintentar')
                continue

        while True: #Ingreso de marca
            marca = input('Ingrese la marca del vehiculo: ')
            if verificar_marca(marca) == True:
                auto['Marca'] = marca
                break
            else:
                print('Datos no validos, reintentar')
                continue
        
        while True: #Ingreso de precio
            precio = input('Ingrese el precio del vehiculo: ')
            try:
                precio = int(precio)
            except:
                print('Datos no validos, reintentar')            
                continue

            if verificar_precio(precio) == True:
                auto['Precio'] = precio
                break
            else:
                print('Datos no validos, reintentar')
                continue

 
        verificacion = input('¿El vehiculo posee multas?(S/N): ') #Verificamos que posea multas
        verificacion = verificacion.upper()
        while True: #Ingreso de multas
            if verificacion == 'S': #Si tiene, ingresamos la fecha y validamos que el valor esté en formato integeR
                fecha_multa = input('Ingrese la fecha de la multa en formato (DD/MM/AA): ')
                monto_multa = input('Ingrese el valor de la multa: ')
                try:
                    monto_multa = int(monto_multa)
                except:
                    print('Los datos deben ser numericos')
                    continue

                auto['Multas']['Fecha'].append(fecha_multa) #Agregamos a la lista los datos de las fechas ingresadas
                auto['Multas']['Monto'].append(monto_multa) #Agregamos a la lista los datos de los valores ingresados

                seguir = input('¿Desea seguir ingresando multas?(S/N): ') #Verificación para saber si el usuario quiere seguir agregando multas
                seguir = seguir.upper()

                if seguir == 'S': #Seguir en el ingreso de multas en caso de generar más
                    continue
                elif seguir == 'N': #Salir del ingreso de multas en caso de no querer seguir
                    break
                else: 
                    print('Datos no validos, reintentar')
                    continue
            
            elif verificacion == 'N': #Salir del ingreso de multas en caso de no tener
                break

        autos.append(auto)        
        ingreso = input('¿Desea seguir ingresando autos? (S/N)')
        ingreso = ingreso.upper()
        if ingreso == 'S':
            continue
        elif ingreso == 'N':
            break

def buscar_vehiculo():
    buscar = input("Ingrese la patente del Vehiculo: ")
    print('Los datos del auto son los siguientes: ')
    for auto in autos:
        if 'Patente' in auto and auto['Patente'] == buscar:
            print(auto)
            break
        else:
            print('La patente ingresada no se encuentra registrada')

def imprimir_certificados():

    certificados = { #Objeto certificados con valores en 0.
    'CONTAMINANTES' : 0,
    'ANOTACIONES VIGENTES' : 0,
    'MULTAS': 0 

    }

    for valor in certificados:
        certificados[valor] = random.randint(1500, 3500) #Randomizar valores de los certificados según rango dado en ejercicio

 
    patente = input('Ingresa la patente del Vehículo: ') 
    for auto in autos:
        if verificar_patente(patente) == True and patente in autos: #Verificacion que cumpla los digitos y que exista en el array de autos
            break
        else:
            print("La patente no cumple las condiciones necesarias")
            continue

    print(f'Los certificados disponibles son los iguientes: ')

    for llave, clave in certificados.items(): #Imprime el objeto certificado de una manera legible
        print(f'{llave} = ${clave}')

    while True:
        certificado_u = input('¿Qué certificado desea imprimir?: ')
        certificado_u = certificado_u.upper()
        if certificado_u in certificados.keys():
            break
        else:
            print('Certificado no disponible')
            continue

    print(f'Su certificado de {certificado_u} se encuentra en cola de impresión... ')
    print(f'La patente del vehiculo es: {patente}')
    for auto in autos:
        if auto['Patente'] == patente:
            dueño = auto['Dueño']
            print('Datos del dueño: ')
            print('Nombre: ', dueño['Nombre'])
            print('Apellido: ', dueño['Apellido'])
            print('RUN: ', dueño['RUN'])
        else:
            print('Patente no se encuentra registrada')
    if certificado_u == 'MULTAS':
        print('Multas del vehiculo')
        for auto in autos:
            if auto['Patente'] == patente:
                multas = auto['Multas']
                print('Fechas: ', multas['Fecha'])
                print('Montos: ', multas['Monto'])
                break

grabar_vehiculo()
buscar_vehiculo()
imprimir_certificados()