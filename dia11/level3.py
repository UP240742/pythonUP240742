#level3
#1
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime(7))

#2
def are_all_items_unique(lst):
    return len(lst) == len(set(lst))

print(are_all_items_unique([1, 2, 3]))

#3
def are_all_items_same_type(lst):
    return all(type(i) == type(lst[0]) for i in lst)

print(are_all_items_same_type([1, 2, 3]))

#4
import keyword

def is_valid_variable(var):
    return var.isidentifier() and not keyword.iskeyword(var)

print(is_valid_variable("my_var"))