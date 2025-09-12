x = "aaaabbcca"

contar = {}
for i in x:
    if i in contar:
        contar[i]+=1
    else:
        contar[i]=1

print(contar)