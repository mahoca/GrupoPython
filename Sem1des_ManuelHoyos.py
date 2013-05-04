
lista=[]
i=1

num=input("Introduce un numero del 1-9 :")
limite=int(num)*2-1
lim=int(num)

for i in range(limite):
    lista.append(i) #crea los elementos de la lista
    lista[i]=0 #rellena la lista con ceros
print(lista)

while x<= lim:
    lista[lim-1]=x
    print(lista)
    x+=1




