def all_substrings_bitwise(s):
    n = len(s)
    substrings = []
    
    # Total possible substrings = n*(n+1)/2
    # Use bitmask to generate substrings
    for start in range(n):
        for end in range(start, n):
            mask = (1 << (end - start + 1)) - 1  # bitmask for substring length
            substring = ""
            for i in range(end - start + 1):
                if mask & (1 << i):  # check if bit is set
                    substring += s[start + i]
            substrings.append(substring)
    
    return substrings

# Example usage
s = input("Enter a string: ")
result = all_substrings_bitwise(s)
print("All substrings are:")
for sub in result:
    print(sub)
