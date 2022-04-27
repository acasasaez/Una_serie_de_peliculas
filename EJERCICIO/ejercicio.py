import numpy as np 
Valoraciones = [0,1,2,3,4,5]
numer_valoraciones = [58,88,124,132,96,42]
lista_recibidor = []
def calcular_lista_recibidora (a, b): 
    for i in range (len(a)): 
        while i<= len(a):
            m = a[i]*b[i]
            lista_recibidor.append(m)
    

calcular_lista_recibidora(Valoraciones, numer_valoraciones)
print (lista_recibidor)
print ("HOLA")