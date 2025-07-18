#level1 
#1
#condiciones 
age = int(input('Enter your age:'))
e = 0
if age >= 18:
    print('You are old enough to learn to drive.')
elif age < 18:
    print('You need more years to learn to drive.') 
#2
#condicional con tres terminos 
you = int(input('Enter your age: '))
me = 18 
if you == me: 
    print('twice')
elif you > me:
    print('you are older than me')
else: 
    print('you are younger than me')
#3
n = int(input('Enter numer one: '))
m = int(input('Enter numer two: '))
if n == m: 
    print('One numer is twice than two')
elif n > m:
    print('One numer is greater than two')
else: 
    print('One numer is smaller than two')
