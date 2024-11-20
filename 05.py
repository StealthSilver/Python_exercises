# Linear Search

def linear_search(arr, target):
    
    for index, value in enumerate(arr):
        if value == target:
            return index  
    return -1


arr = [5, 3, 8, 6, 7, 9, 2]
target = 6

result = linear_search(arr, target)

if result != -1:
    print(f"Element {target} found at index {result}.")
else:
    print(f"Element {target} not found in the list.")