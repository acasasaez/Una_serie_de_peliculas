# Una_serie_de_peliculas
Para esta tarea he hecho lo siguiente: 

1. En primer lugar, probé el comportamiento de las librerías numpy y pandas para entenderlas un poco (sé que este ejercicio podía resolverse sin acudir a este recurso) 

2. A continuación, introduje los datos del problema mdiante un archivo .csv.

3. Después, creé una función que me permitiese obtener los datos que me interesaban y con estos calculé Media, Mediana, Varianza y Desviación típica, gracias a los métodos de Numpy.

4. Por último, escribí un archivo .csv que contuviese la tabla de resultados. 
Dejo a continuación el código para esta parte:
###Primera parte del código
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

Para la segunda parte creé un nuevo archivo donde elaboré una función que me permities obtener el número de estrellas bajo el cual encontramos un determinado porcentaje de votos, es decir calculamos el número de estrellas que cuentan con una determinada frecuencia acumulada. 

### Segunda parte del código: 
```
def DA(a,b, valor_porcentaje):
  
    lista_vacia  =[]
    lista_vacia_2 =[]
    Lista_puente=[]

   
    for i in range (len(a)):#recorremos la lista a 
        m = a[i]*b[i]# multiplicamos los datos de la misma posición en a y b
        lista_vacia_2.append(m)#los añadimos a nuestra lista vacía para consegui
    valor_comparar = sum(lista_vacia_2)*valor_porcentaje/100
    lista_vacia_2.append(0)
    zz=0
    for i in range (len(lista_vacia_2)-1): 
        k=lista_vacia_2[i] + zz
        lista_vacia.append (k)
        zz=lista_vacia[ len(lista_vacia)-1] 
    lista_vacia_2.pop()  
    for i in range (len(lista_vacia)):
        if valor_comparar <= lista_vacia[i]:
             Lista_puente.append(lista_vacia[i])
   
    for i in range (len(lista_vacia)):
        if Lista_puente[0] == lista_vacia [i]:
            return a [i]

```

Finalmente, creé un main donde, mediante la importación de Pandas, se hace la lectura del .csv de los resultados y el número de estrellas que cuentan con el porcentaje de votos acumulados (valor indicado en el enunciado: 68%, 95%,97%)

###Tercera parte del código:
```
from f import* 
 
import pandas as pd 
import numpy 

df = pd.read_csv(r"C:/Users/andre/OneDrive/Escritorio/Programación/Una_serie_de_peliculas/resultados.csv.csv")
print(df)

print ("El 68% de los votos se encuentra en el intervalo [1,",(DA([0,1,2,3,4,5],[58,88,124,132,96,42], 68)),"]")
print ("El 68% de los votos se encuentra en el intervalo [1," ,(DA([0,1,2,3,4,5],[58,88,124,132,96,42], 97)),"]")
print ("El 68% de los votos se encuentra en el intervalo [1,",(DA([0,1,2,3,4,5],[58,88,124,132,96,42],95)),"]")
```
Añadir que la intención inicial era hacer códigos más elaborados donde se incluyesen conocimientos aprendidos a lo largo del curso (recursividad, excepciones...) y terminar con el uso de gráficas con ayuda de matplotlib; pero no conseguía que funcionasen correctamente ninguno de los 2.
