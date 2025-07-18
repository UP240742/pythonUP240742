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



#cadena 
#len= cuenta las letras de la frase 
saludo= ('hola, como estas?')
print(saludo)
print(len(saludo))

#multi cadena 
mil_cade= 'la vida es como el mar, por eso hay que darse como a la espuma'
print(mil_cade)

#concatenacion (suma de datos/numeros)
sal= 'hola'
cor= 'como estas'
sig= '?'
es=' '
salud= sal + es + cor + sig 
print(salud)

#/n= nueva linea 
print('la vida es como el mar.\n por eso hay que darse como a la espuma')

#/t= agrega 8 espacios 
print('hola\tmundo\tpequeño') 
print('hola\t34\t21') 

print('This is a backslash  symbol (\\)')

#\\ = barra invertida(/)
print('hola\\mundo') 

#\' = comilla simple 
print('hola \'mundo') 

#\" = comilla doble se agrega inicio y final para que funcione 
print('hola \"mundo\"')  

#%s = es para identificare una variable sin escibirla 
first_name = 'Asabeneh'
last_name = 'Yetayeh'
language = 'Python'
formated_string = 'I am %s %s. I teach %s' %(first_name, last_name, language)
print(formated_string) 

herm1 = 'cely'
herm2 = 'mome'
herm3 = 'natalia'
hers = 'yo tengo tres hermanos %s %s y %s' %(herm1, herm2, herm3)
print(hers)

#%d = numeros enteros 
#%f = numeros decimales 
r = 21 
pi = 3.14 
area= pi * r **2 
form = 'el area del circulo es: %d por %2f' %(r, pi)
print(area)

#se imprime la aoperacuin y resultado 
a = 4
b = 3
print(f'{a} + {b} = {a +b }')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')

#cadenas la palabra va en vertical una letra por letra 
pal = 'escribir' 
a,b,c,d,e,f,g,h = pal
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)

#[n] = se imprime la letra solicitada entre parentesis 
p = 'programar'
first_letter = p[0] 
print(first_letter)
sexta_letter = p[6]
print(sexta_letter) 
#para empezar de atras para adelante los numeros son negativos 
last_letter =p [-1]
print(last_letter)
segunda_letter =p[-3]
print(segunda_letter)

#utiliza cordenadas para imprimir lo necesario 
l= 'ingeniero'
primer_cuarto= l[0:4]
print(primer_cuarto)

seg = l[3:8]
print(seg)

#tambien se puede aplicar numeros negativos para empezar de atras 
ter = l[-6:-2]
print(ter) 

do = l[0:-5]
print(do)

#[::-1] = invertir cadenas 
fra = 'llaman a la puerta'
print(fra[::-1]) 

#NO FUNCIONA 
#[n:n:n] = los numeros de las letras se quitan 
rf = fra [0:9:4]
print(rf) 

#.capitalize () = para convertir la priera palabra a la mayuscula 
print(fra.capitalize())

#.count('letra') = cuenta las letras de la frase 
print(fra.count('l'))
print(fra.count('a'))

#.endswith() = identificar si lo del parentesis tiene la terminacion 
print(fra.endswith('rta')) 
print(fra.endswith('llam')) 

#.expandtabs(puedees agregar numero)= agregar espacios en cada palabra 
#debe agregar \t en cada espacio de las letras 
rt = 'documental\tde\tnetflix' 
print(rt.expandtabs())
print(rt.expandtabs(12))

#.rfind(letras) = numero de letra que tiene, tambien se cuentan los espacios y empieza a contar desde 0 
frase6='codigo completo'
#identificar cada posiscion de la letra 
print(frase6.rfind('c')) 
print(frase6.rfind('g'))
print(frase6.rfind('l'))

#.format() = juntar variables {}, se suman las variables 
v = 'vaso'
c = 'cucharra'
t = ' tenedor' 
p = 'plato'
mesa= 'me gusta cotar agua en un {}, comer con un {} y {} o {}'.format(v, p, c, t)
print(mesa)

#NO FUNCIONA 
l1= 23 
pi = 20.45
area= pi *l1 **2
res = 'el area del circulo es: {} is {}'.format(str(l1), str(area))
print(res)

#.index() = da la posiscien en la que se necuntra
mus ='el kpop si es musica'
g = 'es'
print(mus.index(g))

#.rindex() = cuenta los epacios que hay antes de llagar a lo solicitado ()
print(mus.rindex(g))
print(mus.rindex(g, 8))
print(mus.rindex('pop'))

#.isalnum() = comprueba caracteres alfanumericos 
w = 'lavidaesbella123'
print(w.isalnum()) #true 
f = 'lavidaesbella'
print(f.isalnum()) #true
q= 'la vida es bella 123'
print(q.isalnum()) #false 
#los espacios no son alfamunericos 

#.isalpha() = compruba caracteres alfabeticos (a - z)
t = 'twiceeselmejorgrupo'
print(t.isalpha()) #true
y = 'twice es el mejor grupo'
print(y.isalpha()) #false, espacios no son alfabeticos 
k = 'twiceeselmejorgrupo123'
print(k.isalpha()) #false, los numeros 

#.isdecimal() = comprueba los carateres de la cadena si son decimales (0-9)
le = 'muchas veces no eliges'
print(le.isdecimal()) #false, no tiene decimales 
ke = '893'
print(ke.isdecimal()) #true, tiene numeros 
mn = '9.43'
print(mn.isdecimal()) #false, decimales no cuentan 
#los espacios tompoco cuentan 

#.isdigit() = identifica numeros y otros caracteres 
lo = 'hola'
print(lo.isdigit()) #false, letras no cuenta 
mu = '543'
print(mu.isdigit()) #true, numeros correcto
si = '\B92'
print(si.isdigit()) #false, caracteres correcto 

#.isnumeric () = comprueba si tiene numeros 
ju = '54'
print(ju.isnumeric()) #true
li = '\H787s'
print(li.isnumeric()) #false 
et = '45.2'
print(et.isnumeric()) #false, decimales no cuentan 

#.isidentifier() = comprueba si tiene un nombre adecuado de cadena_
ta = 'bailemos_toda_la_noche'
print(ta.isidentifier()) #true, importa los__
ej = 'bailemos_toda_la_noche555'
print(ej.isidentifier()) #true, numeros si valen 
al = 'bailemos toda la noche'
print(al.isidentifier()) #false, no tiene__

#.islower() = comprueba si estan en minusculas 
an = 'cookie'
print(an.islower()) #true 
dr = 'Cookie'
print(dr.islower()) #false

#.isupper() = comprueba si TODAS estan en mayusculas 
print(an.isupper()) #false 
print(dr.isupper()) #false 
ra = 'COOKIE'
print(ra.isupper()) #true 

#join(puede estar libre o agregar carater) = devuelve una cadena conectada 
web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = ' '.join(web_tech)
print(result) # 'HTML CSS JavaScript React'
web_tech2= ['HTML', 'CSS', 'JavaScript', 'React']
result = '# '.join(web_tech2)
print(result) # 'HTML# CSS# JavaScript# React'

#.strip() = elimina caracteres del ()
ru = 'momoland'
print(ru.strip('mo'))

#.replace() = emplaza cadena dada 
challenge5 = 'thirty days of python'
print(challenge5.replace('python', 'coding')) 
#(palabra a quitar, palabra nueva)

#.split() = divide la cadena dada 
iz= 'alcohol free'
print(iz.split()) #['alcohol', 'free']
ve = 'alcohol, free'
print(ve.split('.'))

#.title() = minusculas a mayusculas la primera
la = 'kill this love'
print(la.title()) #solo las letras inciales 

#.swapcase() = minusculas a mayusculas TODA la frase 
print(la.swapcase())
sc = 'Kill This Love'
print(sc.swapcase()) #la mayuscula se vuelve minuscula 

#.startswith() = empieza con la letra del ()
co = 'you y me'
print(co.startswith('you')) #true 
print(co.startswith('me')) #false 



#18 
tres = it_companies[4:9]
print(tres)
#19 
tre = it_companies[0:6]

#20 
emp = it_companies[4:6]
print(emp) 
