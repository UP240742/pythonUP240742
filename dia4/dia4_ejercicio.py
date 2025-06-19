#cadena 
#1
#declarar la variable 
letter= 'treinta'
letter1= 'dias'
letter2= 'de'
letter3='python'
#espacio entre cada palabra 
space= ' '
#se realiza la cadena 
cadena= letter + space + letter1 + space + letter2 + space + letter3
print(cadena)

#2
letter4= 'codificacion'
letter5= 'para'
letter6= 'todos'
space=' '
cadena2=letter4 + space + letter5 + space + letter6
#imprime la variable 
print(cadena2)
#3
empresa='codificacion para todos'
#4
print(empresa)
#5
#len: contar letras 
print(len(empresa))
#6
#upper: mayusculas 
print(empresa.upper())
#7
#lower: minusculas 
print(empresa.lower())
#8
print(empresa.capitalize())
print(empresa.title())
print(empresa.swapcase())
#9
#slice: quitar letras 
slice= empresa[13:]
print(slice)
#10
#comprobar si tiene la palabra solicitada 
print(empresa.find('codificacion'))
#11
#cadena 
letter7= 'python'
space= ' '
cadena3= letter4 + space + letter5 + space + letter7
print(cadena3)
#12
f1= 'python for everyone'
#cambias una palabra por otra 
print(f1.replace('everyone', 'all'))
#13
#separar cadenas 
print(empresa.split()) 
#14 
#cadena con espacios 
p1= 'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'
print(p1.split())
#15
#identificar puesto de la palabra 
print(empresa[0])
#16
#ultima palabra de la frase 
ñ=len(empresa)-1
print(empresa[ñ])
#17
#identificar la posicion de la letra 
print(empresa [10])
#18 
#identificacion de la posicion de la letra en la frase 
m1=f1[0]
m2=f1[7]
m3=f1[11]
suma= m1 + m2 + m3 
print(suma)
#19
#se identifica las posiciones de la letra solicitada 
n1=empresa[0]
n2=empresa[13]
n3=empresa[18]
#suma 
suma1= n1 + n2 + n3 
#imprimir 
print(suma1)
#20
frase='coding for all'
#identificar cada posiscion de la letra 
print(frase.rfind('c')) 
#21
print(frase.rfind('f'))
#22
print(frase.rfind('i'))
#23 
#identificar posicion de la palabra 
frase1='You cannot end a sentence with because because because is a conjunction'
print(frase1.rfind('because'))
#24
print(frase1.rfind('because'))
#25
slice2=frase1[0:31]
slice3=frase1[55:]
print(slice2+slice3)
#26
print(frase1.rfind('because')) 
#27
#quitar palabras de la frase 
slice2=frase1[0:31]
slice3=frase1[55:]
print(slice2+slice3)
#28
#empieza con ''
print(empresa.startswith('codificacion'))
#29
#termina con ''
print(empresa.endswith('codificacion'))
#30
#quitar espacios 
esp='   Coding For All      '
print(esp.strip(' '))
#31
h = '30DaysOfPython'
print(h.isidentifier()) 
h2 = 'thirty_days_of_python'
print(h2.isidentifier()) 
#32
w= ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
result= ' # '.join(w)
print(result) 
#join es para separa cadenas con el signo indicado (#)
#33
print('I am enjoying this challenge. \nI just wonder what is next.')
#. \n se utilixa para pasar al sieguiente escalon 
#para colocar \ preciona primero la teca Alt
#34
print('Name\tAge\tCountry\tCity')
print('Asabeneh\t250\tFinland\tHelsinki')
#\t es para agregar 8 espaccios 
#35
radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = 'The area of circle with a radius %d is %.2f.' %(radius, area)
#36
a = 8
b = 6
print(f'{a} + {b} = {a +b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b:.2f}')
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} ** {b} = {a ** b}')











