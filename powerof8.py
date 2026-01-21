def is_power_of_8(n):
    if n <= 0:
        return False
    
    # Keep dividing by 8 while divisible
    while n % 8 == 0:
        n //= 8
    
    # If reduced to 1, it's a power of 8
    return n == 1

# Example usage
num = int(input("Enter a number: "))
if is_power_of_8(num):
    print(num, "is a power of 8")
else:
    print(num, "is NOT a power of 8")
