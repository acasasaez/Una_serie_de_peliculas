Valoraciones = [0,1,2,3,4,5]
Personas =  [58,88,124,132,96,42]
print("imprimir datos")
print (Valoraciones)
print (Personas)
lista_vacia = []
def modificar_lista_vacia (a,b): 
    for i in range (len(a)): 
       m =  a[i]*b[i]
       lista_vacia.append(m)
modificar_lista_vacia (Valoraciones, Personas)
print( lista_vacia)

