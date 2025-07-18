#1
empty_list = list()
#2 
list5= ['Julieta', 'Luis', 'Migue', 'Faby', 'Elian', 'Tamara']
print(list5)
#3
print(len(list5))
#4
print(list5[0])
print(list5[2])
print(list5[4])
#5
mixed_data_type= ['Julieta', '19', '1.70', 'soltera', 'soldado insurgente #503']
print(mixed_data_type)
#6 
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
#7
print(it_companies)
#8
print(len(it_companies))
#9
print(it_companies[0])
print(it_companies[3])
print(it_companies[6])
#10 
it_companies[0] = 'Instagram'
print(it_companies)
#11
it_companies.append('Huawei')
print(it_companies)
#12
it_companies.insert(2, 'Samsung') 
print(it_companies) 
#13
it_companies[2] = it_companies[2].upper()
print(it_companies)
#14
i = '#'.join(it_companies)
print(i)
#15
print('Apple' in it_companies)
#16 
print(sorted(it_companies))
#17 
it_companies.sort(reverse=True)
print(it_companies)
#18 
tres = it_companies[3:9]
print(tres)
#19 
tre = it_companies[0:6]
print(tre)
#20 
emp = it_companies[0:3] 
mp = it_companies[6:9]
print(emp + mp) 
#21
it_companies.pop(0)
print(it_companies)
#22
it_companies.pop(5)
print(it_companies)
#23
it_companies.pop(6)
print(it_companies)
#24
print(it_companies.clear())
#25
del it_companies
#26
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
print(front_end + back_end)
#27
full_stack = front_end + back_end
full_stack.append(('Python','SQL'))
print(full_stack) 
