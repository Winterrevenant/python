def remover_val(lista,val):
    i=0
    while i < len(lista):
        if lista[i]==val:
            lista.pop(i)
        else:
            i+=1
        



n=[3,2,2,3]

remover_val(n,3)
print(n)