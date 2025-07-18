#level2
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#1
#unir dos intersecciones 
u = A.union(B)
print(u)
#2
#interseccion de los datos (iguales)
i = A.intersection(B)
print(i)
#3
#si inteccion (si los dtos de A estan en B)
s = A.issubset(B)
print(s)
#4
#identificar si no tiene datos iguales 
d = A.isdisjoint(B)
print(d)
#5
n = B.union(A)
print(n)
#6
#identificar teminos que solo esta en una interseccio 
f = A.symmetric_difference(B)
print(f)
#7
#eliminar terminos 
A 
del A   

B 
del B 


