#level3
import random 
#1
def shuffle_list(lst):
    shuffled = lst[:]
    random.shuffle(shuffled)
    return shuffled

# Ejemplo de sus uso:
print("La shuffled list es:", shuffle_list([1, 2, 3, 4, 5]))