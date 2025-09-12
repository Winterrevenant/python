digits=[1,2,3]

#join une las cadenas sin especios
#map le aplica una funcion a toda la cadena

digits=int("".join(map(str,digits)))
digits=digits+1
digits=[int(i) for i in str(digits)]

print(digits)