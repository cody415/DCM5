def reverse_bits(num, bit_size=32):
    # Convert number to binary with fixed size
    binary = format(num, f'0{bit_size}b')
    # Reverse the binary string
    reversed_binary = binary[::-1]
    # Convert back to integer
    return int(reversed_binary, 2)

# Example usage
num = int(input("Enter a number: "))
new_num = reverse_bits(num, 8)  # You can change bit_size (8, 16, 32)
print("Original number:", num)
print("New number after reversing bits:", new_num)
