# listas
a=[2,4,6,8,10,12]
b=[2,10.5,"Jose",True]
c=[2,4,6,a,6,7]
d=[2,3,4,[1,2,3,4,5],6]
print(a)
print(b)
print(c)
print(d)
a.append(14)
print("---------")
print(a)
print(b)
print(c)
aux=a[3]
print("Valor de la pos 3 de a ",aux)
print("Tamaño de c",len(c))
print("Tamaño de c",len(c[3]))
print("elemento de d sub lista pos 1",d[3][1])
