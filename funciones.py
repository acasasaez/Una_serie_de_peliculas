def distribucion_acumulada (a,b):
  #Necesitamos una lista donde guardar las frecuencias acumuladas
    lista_fa= [b[0]]

    
    for i in range (len(b)):
        while i+1<=len(b):
            a =b[i+1] +b[i] 
            lista_fa.append(a)
            
    return (lista_fa)
print (distribucion_acumulada([0,1,2],[1,2,3]))
print ("hola")