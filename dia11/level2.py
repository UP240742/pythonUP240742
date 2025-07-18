#level2
#1
def evens_and_odds(n):
    evens = len([i for i in range(n + 1) if i % 2 == 0])
    odds = n + 1 - evens
    print(f'The number of odds are {odds}.')
    print(f'The number of evens are {evens}.')
evens_and_odds(100)
#2
def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
print(factorial(5))
#3
def is_empty(param):
    return not bool(param)
print(is_empty([]))
#4
import statistics

def calculate_mean(lst):
    return statistics.mean(lst)

def calculate_median(lst):
    return statistics.median(lst)

def calculate_mode(lst):
    return statistics.mode(lst)

def calculate_range(lst):
    return max(lst) - min(lst)
def calculate_variance(lst):
    return statistics.variance(lst)

def calculate_std(lst):
    return statistics.stdev(lst)

data = [1, 2, 2, 3, 4, 5, 5]

print("Mean:", calculate_mean(data))        
print("Median:", calculate_median(data))     
print("Mode:", calculate_mode(data))         
print("Range:", calculate_range(data))       
print("Variance:", calculate_variance(data)) 
print("Std Dev:", calculate_std(data))
