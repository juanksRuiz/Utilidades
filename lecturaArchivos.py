#-*- coding: utf-8 -*-
def separarDatos(ch,linea):
#Separa los datos de la linea cada vez que encuentre ch
    sep = []
    dato = ''
    i = 0
    if linea == '':
        return ['']
    elif linea == ch:
        return[]
    else:
        while (i < len(linea) -1):               
            if (linea[i] != ch):
                dato = dato + linea[i]
                i = i+1
            else:
                sep.append(dato)
                dato = ''
                i = i+1
        if linea[i] == '\n':
            sep.append(dato)
        else:
            dato = dato + linea[i]
            sep.append(dato)
        return sep
            
def lineaLatex(datos):
#Esribe la lista datos en una linea para tablero en formato Latex
    # en este caso, los distintos datos están ya en una lista
    if len(datos) == 0:
        print " ERROR: no hay datos en la lista ingresada"
        return
    else:
        output = '%s'
        if len(datos) > 1:
            for i in range(1,len(datos)):
                if i != (len(datos) -1):
                    output = output + '&%s'
                elif (i == (len(datos)-1)):
                    output = output + '&%s'+'\\' + '\\' + ' \\hline'
        else:
            output = output + '\\' + '\\'
        # Afuera de la función la persona elije los datos y su orden
        return output


def DatosALatex(listaDatos):
    #Dada una lista de listas de valores sacadas Tracker, escribe las listas en formato Latex
    #Primero Buscar las lineas necesarias en el txt, luego llamar a la funcion con esas lineas
    for entrada in listaDatos:
        s = entrada.replace(',','&')
        print (s + '\\' + '\\' + ' \\hline')

tiempo = [i for i in range(10)]
y = [i**2 for i in tiempo]
v = []
for i in range(len(tiempo)):
    v.append(5.3*i)

final =[tiempo,y,v]

DatosALatex(final)






"""
lin1=  "Juan Camilo Ruiz,19,MACC,2017-2"
lin2 = "Daniel Felipe Rambaut Lemus,20,MACC,2017-2"
todo = [lin1,lin2]

for i in range(2):
    datos = separarDatos(',',todo[i])
    output = lineaLatex(datos)
    print output %(datos[0],datos[1],datos[2],datos[3])
"""
#############################################
"""
d = 'C:\Users\juank\Desktop\lectura.txt'
f = open(d,'r')
st = StringTokenizer('&')
#read() escribe todo el ocntenido
#mensaje = f.read()
todo = []
lineas = f.readlines()
for a in lineas:
    todo.append(st.separarDatos(a))
for i in todo:
    print i
"""
