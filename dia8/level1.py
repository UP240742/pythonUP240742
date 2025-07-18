#level1
#1 y 2 
#crear un diccionario 
dog = {}
#2
#agregar datos al diccionario 
dog['name'] = 'Michi'
dog['color'] = 'cafe'
dog['raza'] = 'pug'
dog['age'] = 'tres'
print(dog)
#3
student = {'first_name':'Julieta','last_name':'Ruiz', 'gender': 'femenino', 'age':'19', 'marital_status,':'soltera', 'skills':'leer', 'country':'Mexico', 'city':'Mexico', 'address':'morelos1'}
#4
print(len(student))
#5
#como 'convertir' a lista el dic.
s = student.keys()
print(s)
#6
#modificar datos 
student['skills'] = 'conversar'
print(student)
#7
#convertir la dirreccion a lista de tuple
t = student.items()
print(t)
#8
#cambiar los valores de diccionario a lista 
u = student.values()
print(u) 
#9 
d = student.items()
print(d)
#10
#limpiar el diccionario 
e = student.clear()
print(e)
#11
#eliminar diccionario 
student 
del student




