#level1
#declarar variables pero el usuario

first_name=input('Julieta')
last_name=input('Ruiz')
full_name=input('Julieta Alejandra Ruiz Velasco')
contry=input('Mexico')
city=input('Aguascalientes')
age=input('18')
year=input('Años')
is_married=input('Soletra')
is_true=input('Es verdad')
is_light_on=input('Luz encedida')
a,b,c= input('Ingrese tres valores:').split()   #variables 

#level 2 
#imprimir las variables 
print(type(first_name))
print(type(last_name))
print(type(full_name)) 
print(type(contry))
print(type(city)) 
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(a))
print(type(b))
print(type(c))


#identifica el valor minimo 
print(min(4, 45, 65, 1))
print(type(min([4, 45, 65, 1])))

#identifica el valor maximo 
print(type(max([5, 73, 15])))
print(max(5, 73, 15))

#suma de valores 
print(sum([32, 56, 13]))

#imprimir y contar la variable 
print(len('Hola mundo')) 

#declarar varias variables en una sola linea 
nombre, edad, apellido = 'julieta', 19, 'ruiz'
print(nombre, edad, apellido)
print(nombre)

#se agrega lo que estaa dentro de los parentesis 
print('hola', ',', 'world', '!')

#input= es para que el usuario pueda ingresar informacion 
name=input('Cual es tu nombre?')
print(name)

#float= numeros decinales 
l= 56.56
print(float(l))

#int= numeros enteros 
# quita los decimales NO los redondea los quita 
m= 45.78
print(int(m))

#str= numeros con decimal y enteros 
n= 34
print(str(n))

#espacios con coma en cada letra   
a= 'Celina'
print(a)
a_to_list= list(a)
print(a_to_list)






