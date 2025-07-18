#level1
#1 
#ejecuta uno en cada renglon del 0-10  
for number in range(0, 11):
    print(number) 
#en una lista con []
lst = list(range(0, 11, 1)) 
print(lst)
#2 MAL ESTRUCTURA 
l = list(range(11, 0, 1)) 
print(l)

for num in range(11, 0):
    print(num) 
#3
for i in range(1, 8):
    print('#' * i)
print('-----')
#4
for i in range(8):
    for j in range(8):
        print('#', end=' ')
    print()
print('-----')
#5
n=0
while n<=10:
    r= n*n
    print(n,'x',n,'=',r)
    n= n+1
print('-----')
#6
technologies = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']

for tech in technologies:
    print(tech)
print('-----')
#7
for number in range(0, 101):
    if number % 2 == 0:
        print(number)

print('-----')
#8
for number in range(0, 101):
    if number % 2 != 0:
        print(number)
