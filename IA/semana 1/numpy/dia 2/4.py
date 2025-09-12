import numpy as np

a=np.arange(1,17)
a=a.reshape(4,4)

#Extraer la diagonal principal
for i in range(0,4):
    print(a[i,i],end=",")
print()


#Converit ultima fila en 0

a[-1:]=0
#Extraer sub matriz del centro manual
submatriz=np.array([
    [a[1,1],a[1,2],a[1,3]],
    [a[2,1],a[2,2],a[2,3]]
])
#Con Slicing
submatri1=np.array([
    a[1,1:4],
    a[2,1:4],
   
    
])
print(a)
print(submatriz)
print(submatri1)