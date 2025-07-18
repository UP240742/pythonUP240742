#level3
#1
countries=[]
land_countries = []

for country in countries:
    if 'land' in country:
        land_countries.append(country)

print("Countries containing 'land':", land_countries)

print('-----')
#2
fruits = ['banana', 'orange', 'mango', 'lemon']
reversed_fruits = []

for i in range(len(fruits) - 1, -1, -1):
    reversed_fruits.append(fruits[i])

print("Reversed list:", reversed_fruits)
