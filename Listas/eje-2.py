a=[2,4,6,8,10,12]
n=0
while n<len(a):
    print("a[",n,"] =",a[n])
    n=n+1 
# ahora con for
for x in a:
    print("[",x,"]")
i=1   
for x in a:
    i=i+1
    if i%2==0:
        print("[",x,"]")
