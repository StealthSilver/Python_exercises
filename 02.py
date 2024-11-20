# Square root by newton raphson method

def newton_raphson_sqrt(n, tolerance=1e-10, max_iterations=1000):
    
    x = n / 2.0
    iteration = 0

    while iteration < max_iterations:
        
        x_new = 0.5 * (x + n / x)
        
        
        if abs(x_new - x) < tolerance:
            return x_new
        
  
        x = x_new
        iteration += 1
    
    
    return x


num1 = 25
num2 = 49

sqrt_num1 = newton_raphson_sqrt(num1)
sqrt_num2 = newton_raphson_sqrt(num2)

print(f"Square root of {num1} is approximately {sqrt_num1}")
print(f"Square root of {num2} is approximately {sqrt_num2}")