#level2
#1
u = int(input('Enter students scores:'))
e = 0
if u > 90 and u <= 100:
    print('A')
elif u > 80 and u < 89:
    print('B') 
elif u >  70 and u < 79:
    print('C')
elif u > 60 and u < 69:
    print('D')
elif u > 50 and u < 59:
    print('E')
elif u > 0 and u < 49:
    print('F')
#2
mes = input('Enter a month:').capitalize()
if mes in ["September", "October", "November"]:
    print('The season is Autumn')
elif mes in ["December", "January", "February"]:
    print('The season is Winter')
elif mes in ["March", "April", "May"]:
    print('The season is Spring')
elif mes in ["June", "July", "August"]:
    print('The season is Summer')
else:
    print('error')
#3
frutas = ['banana', 'orange', 'mango', 'lemon']
fruta= input('Enter a fruit:')
if (fruta in frutas) == True:
    print('The fruit already exist in the list')
else:
    frutas.append(fruta)
    print(frutas)
    

