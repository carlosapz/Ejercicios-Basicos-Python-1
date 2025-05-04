num = int(input('Digite un numero entero positivo:'))
aux = num
menor = num
while num >= 1:
  aux = num % 10
  if aux < menor:
    menor = aux
  num = num/ 10
print('Digito menor:' ,menor)