#level1
#1
#declarar dos variables y sumarlos 
def add_two_numbers ():
    num_one = 2
    num_two = 7
    total = num_one + num_two
    return total
print(add_two_numbers())
#2
def area_of_circle (r):
    PI = 3.14
    area = PI * r ** 2
    return area
print(area_of_circle(10))
#3
add_all_nums = input('Ingresa un numero')
def add_all_nums(n):
    total = 0
    for i in range(n+1):
        total+=i
    print(total)
#4
def convert_celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
print(convert_celsius_to_fahrenheit(100))
#5
def check_season(month):
    month = month.lower()
    if month in ['september', 'october', 'november']:
        return 'Autumn'
    elif month in ['december', 'january', 'february']:
        return 'Winter'
    elif month in ['march', 'april', 'may']:
        return 'Spring'
    elif month in ['june', 'july', 'august']:
        return 'Summer'
    else:
        return 'Invalid month'  
print(check_season('may'))
#6
def calculate_slope(x1, y1, x2, y2):
    if x2 == x1:
        return "Slope is undefined (division by zero)"
    return (y2 - y1) / (x2 - x1)
print(calculate_slope(1,2,3,4))
#7
import cmath
def solve_quadratic_eqn(a, b, c):
    d = cmath.sqrt(b**2 - 4*a*c)
    x1 = (-b + d) / (2*a)
    x2 = (-b - d) / (2*a)
    return x1, x2
print(solve_quadratic_eqn(5,8,2))
#8
def print_list(lst):
    for item in lst:
        print(item)
print(print_list([1,2,3,4]))
#9
def reverse_list(lst):
    reversed_lst = []
    for i in range(len(lst)-1, -1, -1):
        reversed_lst.append(lst[i])
    return reversed_lst
print(reverse_list([9,8,7,6]))
#10
def capitalize_list_items(lst):
    return [item.capitalize() for item in lst]
print(capitalize_list_items(['potato', 'tomato']))
#11
def add_item(lst, item):
    lst.append(item)
    return lst
food = ['Potato', 'Tomato', 'Mango']
print(add_item(food, 'Milk'))
#12
def remove_item(lst, item):
    if item in lst:
        lst.remove(item)
    return lst
print(remove_item(food, 'Tomato'))
#13
def sum_of_numbers(n):
    return sum(range(n + 1))
print(sum_of_numbers(9))      
#14
def sum_of_odds(n):
    return sum(i for i in range(n + 1) if i % 2 != 0)
print(sum_of_odds(10))
#15
def sum_of_even(n):
    return sum(i for i in range(n + 1) if i % 2 == 0)
print(sum_of_even(10))