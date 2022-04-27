# Una_serie_de_peliculas
Para esta tarea he hecho lo siguiente: 

1. En primer lugar, probé el comportamiento de las librerías numpy y pandas para entenderlas un poco (sé que este ejercicio podía resolverse sin acudir a este recurso) 

2. A continuación, introduje los datos del problema mdiante un archivo .csv.

3. Después, creé una función que me permitiese obtener los datos que me interesaban y con estos calculé Media, Mediana, Varianza y Desviación típica, gracias a los métodos de Numpy.

4. Por último, escribí un archivo .csv que contuviese la tabla de resultados. 

Dejo a continuación el código para esta parte:
```
Valoraciones = [0,1,2,3,4,5]
Personas =  [58,88,124,132,96,42]
print("imprimir datos")
print (Valoraciones)
print (Personas)
lista_vacia = []
#Necesitamos sacar los datos para cálculo a partir de los datos aportados por el problema 
#para ello creams os una función que se ajuste a los datos con los que contamos 
def modificar_lista_vacia (a,b): 
    for i in range (len(a)):#recorremos la lista a 
       m = a[i]*b[i]# multiplicamos los datos de la misma posición en a y b
       lista_vacia.append(m)#los añadimos a nuestra lista vacía para conseguir la lista de datos que emplearemos finalmente
modificar_lista_vacia (Valoraciones, Personas)
print( lista_vacia)

from fileinput import close
import numpy as np
Media = np.mean(lista_vacia)
Mediana = np.median(lista_vacia)
Desviacion = np.std(lista_vacia)
Varianza = np.var(lista_vacia)
print (Media, Mediana, Desviacion, Varianza)


mis_datos_1= [["Valoraciones:""Personas:"],
[0, 58],
[1,88],
[2,124],
[3,132],
[4,96],
[5,42]]
mis_datos_2 =[ ["Media", "Mediana","Desviacion","Varianza"], 
[Media, Mediana, Desviacion, Varianza],]
import csv
with open("resultados.csv.csv", "w",newline = "") as file: 
    writer =csv.writer(file, delimiter = "," )
    writer.writerow( ["TABLA DE DATOS RESULTADOS"])
    writer.writerows(mis_datos_2)
    ```
