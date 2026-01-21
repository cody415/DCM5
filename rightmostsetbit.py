def rightmost_set_bit(n):
    if n == 0:
        return "No set bit (number is 0)"
    
    # Isolate the rightmost set bit
    rmb = n & -n
    return rmb

# Example usage
num = int(input("Enter a number: "))
print("Rightmost set bit value is:", rightmost_set_bit(num))
