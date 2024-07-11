from random import * 
import os
import time
import csv

def limpiar():
    os.system('cls')

def menu():
    print(''' 
    1. Asignar sueldos aleatorios
    2. Clasificar sueldos
    3. Ver estadísticas.
    4. Reporte de sueldos
    5. Salir del programa ''')

sueldosprimeros=[]
sueldossegundos=[]
sueldosterceros=[]
sueldos=[]
trabajadores=["Juan Pérez”,”María García”,”Carlos López”,”Ana Martínez”,”Pedro Rodríguez”,”Laura Hernández”,”Miguel Sánchez”,”Isabel Gómez”,”Francisco Díaz”,”Elena Fernández"]


def asignarsueldosaleatorios():
        numero=0
        acceso=1
        while acceso==1:
            sueldo=randint(300000,2500000)
            sueldos.append(sueldo)
            numero+=1
            if numero==10:
                print(sueldos)
                acceso=2
                        

        
def clasificarsueldos(sueldos):
        for sueldo in sueldos:
            if sueldo<800000:
                sueldosprimeros.append(sueldo)
            elif 800000<sueldo<2000000:
                sueldossegundos.append(sueldo)
            elif sueldo>2000000:
                sueldosterceros.append(sueldo)
                
        cantidad1=len(sueldosprimeros)
        print(f''' SUELDOS MENORES A 800.000: {cantidad1}
                {sueldosprimeros} ''')
        print()
        cantidad2=len(sueldossegundos)
        print(f''' SUELDOS MAYOR A 800.000 Y MENORES DE 2.000.000: {cantidad2}
            {sueldossegundos}''')
        print()
        cantidad3=len(sueldosterceros)
        print(f''' SUELDOS MAYORES A 2.000.000: {cantidad3}
            {sueldosterceros}''')
        
            
            


def verestadisticas(promedio):
    maximo=max(sueldos)
    minimo=min(sueldos)
    numero=sum(sueldos)
    cantidad=len(sueldos)
    promedio=numero/cantidad
    print(f'''
            EL MAYOR SUELDO ES {maximo} 
            EL MENOR SUELDO ES {minimo}
            EL PROMEDIO DE SUELDO ES {promedio}''')




def reportedesueldos():
    limpiar()
    with open('archivoexamen.csv','w',newline='') as archivoexamen_csv:
        contenido=csv.writer(archivoexamen_csv)
        contenido.writerow(['Nombre Empleado','Sueldo base','Descuento Salud','Descuento AFP','Sueldo liquido'])
        contenido.writerow([' solo llege hasta aqui'])
        time.sleep(1)        

        
        



def menuprincipal():
    limpiar()
    menu()
    acceso=1
    while acceso==1:
        try:
            opc=int(input(' escoje tu opcion (1-4):     '))
        except ValueError:
            print(' opcion equivocada, reintente.   ')
            continue
        if opc==1:
            limpiar()
            asignarsueldosaleatorios()
            deseasseguir()
        elif opc==2:
            limpiar()
            clasificarsueldos(sueldos)
            deseasseguir()
        elif opc==3:
            limpiar()
            verestadisticas(sueldos)
            deseasseguir()
        elif opc==4:
            limpiar()
            reportedesueldos()
            deseasseguir()
        elif opc==5:
            print(''' 
            Finalizando programa…
            Desarrollado por Luis Fuentes
            RUT 21-145-490-3 ''')
            time.sleep(2)
            break 



def deseasseguir():
    acceso=1
    while acceso==1:
        try:
            opc=int(input(''' Deseas volver al menu principal ?
                          1) Si, volver al menu.
                          2) No, salir                       '''))
        except ValueError:
            print(' opcion equivocada')
            continue
        if opc==1:
            menuprincipal()
        elif opc==2:
            print(''' 
            Finalizando programa…
            Desarrollado por Luis Fuentes
            RUT 21-145-490-3 ''')
            time.sleep(2)
            quit() 










menuprincipal()