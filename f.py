
from re import I


def DA(a,b, valor_porcentaje):
    b.append(0)
    lista_vacia  =[]
    Lista_puente=[]
    for i in range (len(b)-1): 
        k=b[i]*a[i] + b[i-1]*a[i-1]
        lista_vacia.append (k)
    b.pop()

    valor_comparar = (sum(a)*valor_porcentaje)/100
    
    for i in range (len(lista_vacia)):
        if lista_vacia [i] >= valor_comparar:
           Lista_puente.append(lista_vacia[i]) 
   
    for w in range (len (b)):
        if Lista_puente [0] == lista_vacia[w]:
            m =w  
            return a[m]
print (DA([1,2,3,6,9],[1,1,1,1,1], 50))
   #    for w in range (len (b)):
      #  if Lista_puente [0] == b[w]:
       #     m =w 
         #   return a[m]