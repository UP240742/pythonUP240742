#level2
#1
#2
origen = ('Leche', 'Queso', 'Pollo')
vegetales = ('Zanahoria', 'Calabaza', 'Brocoli')
frutas = ('Durazno', 'Kiwi', 'Fresa')
food_stuff_tp = origen + vegetales + frutas
print(food_stuff_tp)
#3
#convertir de tuple a list
n = list(food_stuff_tp)
print(n) 
#4 
#imprimo terminos del medio
medio = food_stuff_tp[3:6]
print(medio)
#5
#imprimir 3 primeros y 3 ultimos 
primeros = food_stuff_tp[0:3]
ultimos = food_stuff_tp[6:9]
pym = primeros + ultimos
print(pym)
#6
#eliminar tuple
food_stuff_tp = (pym) 
del food_stuff_tp
#7
#identificar si el termino este en la tuple
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)