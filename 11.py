# Armstong number

def is_armstrong_number(num):
    digits = str(num)
    num_digits = len(digits)
    sum_of_powers = sum(int(digit) ** num_digits for digit in digits)
    
    return sum_of_powers == num

num = 153
print(is_armstrong_number(num))