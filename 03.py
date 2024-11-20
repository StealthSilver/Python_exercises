# Exponent of a number

def exponentiation(base, exponent):
    
    if exponent == 0:
        return 1
   
    elif exponent > 0:
        return base * exponentiation(base, exponent - 1)
    
    else:
        return 1 / exponentiation(base, -exponent)

base = 2
exponent = 3
result = exponentiation(base, exponent)
print(f"{base} raised to the power of {exponent} is {result}")