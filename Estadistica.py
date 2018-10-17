def promedio(valores):
    #Retorna el promedio de los valores ingresados
    suma = 0
    for v in valores:
        suma = suma + float(v)
    return suma/(len(valores))

def varianza(valores):
    #Retorna la varianza de los valores ingresados
    mean = promedio(valores)
    sumDist = 0
    for v in valores:
        sumDist = sumDist + (v-mean)**2
    return sumDist
    
def sd(valores):
    #Retorna la desviacion estandar de los valores ingresados
    mean = promedio(valores)
    sumDist = 0
    for v in valores:
        sumDist = sumDist + (v-mean)**2

    sd = sumDist**(1.0/2.0)
    return sd



