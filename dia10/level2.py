#level2
#1
total = 0
for number in range(101):
    total += number

print("The sum is:", total)
print('-----')
#2
sum_even = 0
sum_odd = 0

for number in range(101):
    if number % 2 == 0:
        sum_even += number
    else:
        sum_odd += number

print("Sum of even numbers:", sum_even)
print("Sum of odd numbers:", sum_odd)
