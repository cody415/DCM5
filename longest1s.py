def longest_consecutive_ones(n):
    # Convert to binary string (without '0b')
    binary_str = bin(n)[2:]
    
    # Split by '0' to isolate groups of consecutive 1s
    groups = binary_str.split('0')
    
    # Find the longest group length
    longest = max(len(group) for group in groups)
    
    return longest

# Example usage
num = int(input("Enter a number: "))
print("Binary representation:", bin(num)[2:])
print("Longest consecutive 1’s length:", longest_consecutive_ones(num))
