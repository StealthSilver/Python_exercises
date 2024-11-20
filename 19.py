# swap numbers

def swap_numbers(a, b):
    temp = a
    a = b
    b = temp
    return a, b

a = 5
b = 10
a, b = swap_numbers(a, b)
print(f"After swapping: a = {a}, b = {b}")

a, b = swap_numbers(a, b)
print(f"After reversing: a = {a}, b = {b}")