print("hola")
def DA(a,b):
    lista_vacia =[b[0]]
    for i in range (len(b)): 
        while (i+2) < len(b):
            a = b[i+1]+b[i]
            lista_vacia.append(a)
    return(lista_vacia) 
print (DA([1,2,3],[1,2,3]))
print ("jejeje")