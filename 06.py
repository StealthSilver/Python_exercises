# Selection Sort

def binary_search(arr, target):
    
    left, right = 0, len(arr) - 1
    
    
    while left <= right:
      
        mid = left + (right - left) // 2
        
       
        if arr[mid] == target:
            return mid 
        
        
        elif arr[mid] > target:
            right = mid - 1
        
       
        else:
            left = mid + 1
    
    return -1  


arr = [1, 3, 5, 7, 9, 11, 13, 15]
target = 7

result = binary_search(arr, target)

if result != -1:
    print(f"Element {target} found at index {result}.")
else:
    print(f"Element {target} not found in the list.")