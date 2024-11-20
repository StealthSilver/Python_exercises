# mamximum from the list

def find_max_value(numbers):
    
    max_value = numbers[0]
    
    
    for num in numbers:
        if num > max_value:
            max_value = num
            
    return max_value


numbers = [3, 5, 7, 2, 8, 1, 9]
result = find_max_value(numbers)
print(f"The maximum value in the list is: {result}")