#level 2
#variable, acomodo, minimo, maximo 
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24] 
ages.sort()
print(ages)
i = min(ages)
a = max(ages)
print(i)
print(a)
#agregar numeros a la lista 
ages.append(19)
ages.append(26) 
print(ages)

#promedio 
p= sum(ages) / len(ages)
print(p) 

#comprovar 
l = abs(i - p) 
print(l)
k = abs(a - p)
print(k)
