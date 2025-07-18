#level1
#1
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negative_and_zero = [num for num in numbers if num <= 0]
print("La lista con solo negativos y cero es:", negative_and_zero)
#2
list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flattened_list = [num for sublist1 in list_of_lists for sublist2 in sublist1 for num in sublist2]
print("La dimensional list es:", flattened_list)
#3
tuples_list = [(i, 1, i, i**2, i**3, i**4, i**5) for i in range(11)]
print("La lista tuple es:", tuples_list)
#4
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
flattened_countries = [[country.upper(), country[:3].upper(), capital.upper()] for sublist in countries for (country, capital) in sublist]
print("La nueva lista es:", flattened_countries)
#5
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
countries_dict = [{'country': country.upper(), 'city': capital.upper()} for sublist in countries for (country, capital) in sublist]
print("El diccionarios es:", countries_dict)
#6
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
names_concatenated = [' '.join([name[0].upper(), name[1].upper()]) for sublist in names for name in sublist]
print("La lista de strings concatenados es:", names_concatenated)
#7
slope = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1) if x2 != x1 else None
y_interc= lambda x, y, m: y - m * x if m is not None else None
print(f"La pendiente es: {slope(2, 3, 4, 7)}")
print(f"La intersección es: {y_interc(2, 3, slope(2, 3, 4, 7))}")
print(f"La intersección es: {y_interc(4, 7, slope(2, 3, 4, 7))}")
print(f"La intersección es: {y_interc(0, 0, slope(2, 3, 4, 7))}")
print(f"La intersección es: {y_interc(2, 3, slope(2, 3, 4, 7))}")

