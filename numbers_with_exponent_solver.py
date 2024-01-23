# Exercise 15: Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp.

def exponent(base, exp):
    # Check if exp is a non-negative integer
    if not isinstance(exp, int) or exp < 0:
        return "Exponent must be a non-negative integer"
    
    result = 1
    for _ in range(exp):
        result *= base

    return result

# Test cases
base = 2
exp = 3
result = exponent(base, exp)
print(f"{base} raised to the power of {exp} is: {result}")

base = 5
exp = 0
result = exponent(base, exp)
print(f"{base} raised to the power of {exp} is: {result}")
