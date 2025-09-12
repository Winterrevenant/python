def reemplazar_negativos(lista):
   i=1
   while i< len(lista):
      if lista[i] == lista[i-1]:
         lista.pop(i)
      else:
         i+=1  
   return len(lista)       
            
            

numeros = [0,0,1,1,1]

reemplazar_negativos(numeros)
print(numeros) 
