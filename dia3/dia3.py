#declrar diable
import math 
#1,2,3
age=('18')  #numero entero 
height=1.70
Complex_number=5j  #numero complejo 

#4
#declarar las variables de una area 
b=int(input('base')) 
h=int(input('altura'))
#utilizar las variables para el area 
area=0.5*b*h 
print('el area del triangulo es:', area) 

#5
#declarar variables para el perimetro 
a=int(input('primer lado:'))
b=int(input('segundo lado:'))
c=int(input('tercer lado:'))
#utiliza las variables para el perimetro 
perimetro=(a+b+c)
print('El perimetro del triangulo es:', perimetro)

#6
#declara variables 
length=int(input('largo:'))
width=int(input('ancho:'))
#area y perimetro 
area=(length * width)
print('el area es:', area)
perimeter=2*length * width
print('el perimetro es:', perimetro)

#7
#declara variables
radio=int(input('radio'))
pi=('3.1416') 
#area y circunferencia 
area=(pi * radio * radio) #formula 
print('el radio es:', area) #imprimir resultado de la formula 
circumference=(2 * pi *radio)
print('la circuenferencia es:', circumference)

#8
slope=2
y_intercept=-2
x_intercept=1

#9
x1, y1 = 2, 2
x2, y2 = 6, 10
slope2 = ((y2 - y1)/(x2 - x1))
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

#10
print(slope==slope2)

#11
x=-3
y=(x ** 2 + 6 * x + 9)

#12
#declarar las variables 
p='python'
d='dragon'
#len identificar cuantas palabras ahi  
lenght1=len('p')
length2=len('d')
#imprimimos los resultados 
print('las palabras que tiene son:', lenght1)
print('las palabras qur tiene son:', length2)
print('la comparacion es:', lenght1==length2)

#13
n=("on" in "dragon" and "on" in "python")
print("Is 'on' in both 'python' and 'dragon'?", n) 

#14
jargon=("jargon" in "I hope this course is not full of jargon")
print("Is 'jargon' in the sentence 'I hope this course is not full of jargon'?", jargon)

#15
ont=('on' not in 'dragon' and 'on' not in 'python')
print("There is no 'on' in both dragon and python", ont)

#16
lengtht_python=len('python')
print(float(lengtht_python))
print(str(lengtht_python))
#str definir una cadena 

#17
numero=int(input('ingrese un numero par:'))
numero_par=(numero % 2 == 0)
print('su numero es par:', numero_par ) 

#18 
comparacion=(7 // 3 == int(2.7))
print('la divicion entre el 7 y 3 es equivalente 2.7', comparacion)

#19 
tipo=(type('10') == 10)
print('el tipo 10 es equivalente a 10', type)

#20
n=(int(float('9.8')) == 10)
print("int('9.8') is equal to 10", n)

#21
horas=int(input('ingrese las horas:'))
pagar=int(input('ingrese la tarifa por hora:'))
print('ganacias semanales son:', horas*pagar)

#22
años= int(input('ingrese años vividos:'))
segundos= años * 365 * 24 * 60 * 60
print('has vivido por:', segundos, "segundos.")

#23
print("1 1 1 1 1")
print("2 1 2 4 8")
print("3 1 3 9 27")
print("4 1 4 16 64")
print("5 1 5 25 125")



#boolean 

#verdadero o falso SIEMPRE en mayuscculas la primera letra 
print(True)
print(False)

#se  realiza la operacion con la palabra en entre comillas 
print('suma', 7 + 2)

#se compara dos numeros 
#se imprime con True o False 
print(3 > 2)     # True, 3 es MAYOR que 2
print(3 >= 2)    # True, 3 es MAYOR que 2
print(3 < 2)     # False, 3 no es MAYOR que 2 
print(2 < 3)     # True, 2 es MENOR que 3
print(2 <= 3)    # True, 2 es MENOR que 3
print(3 == 2)    # False, 3 no es IGUAL a 2
print(3 != 2)    # True, 3 no es IGUAL a 2

#se cuentas las letras y se evaluan y se clasifica con True o False 
print(len('mango') == len('avocado'))
print(len('milk') != len('meat'))

#is= verdad si ambas variables son el mismo 
print('1 is 1')

#is not= verdad si ambas variables no son las mismas 
print('1 is not 2')

#in= identifica si el termino esta en la frase (aplica tambien con numeros)
print('dior' in 'christian dior')

#and= True, por que ambos son verdaderos 
print(3 > 2 and 4 > 3)
#falso
print(3 > 2 and 4 < 3)

#or= True, porque ambos son veredaderos 
print(3 > 2 or 4 > 3)  
#falso 
print(3 > 2 or 4 < 3)





