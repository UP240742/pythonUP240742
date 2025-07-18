#level1 
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

#1 
print(len(it_companies))
#2
#agregar solo un termino
it_companies.add('Twitter')
print(it_companies)
#3 
#agregar multiples terminos 
com = ('Samsung', 'Huawei', 'Lenovo', 'Hp')
it_companies.update(com)
print(it_companies)
#4
#quitar terminos (puede cometer errores)
one = ('Apple')
it_companies.remove(one)
print(it_companies)
#5
#quita terminos (sin errores)
d = ('Google')
it_companies.discard(d)
print(it_companies)


