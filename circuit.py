def compute_output(A, B, C):
    # Step-by-step bitwise logic
    AND1 = A & B
    OR1 = B | C
    AND2 = OR1 & C
    AND3 = AND2 & OR1
    Q = AND1 | AND3
    return Q

# Example usage
# You can change A, B, C to 0 or 1
A = int(input("Enter value for A (0 or 1): "))
B = int(input("Enter value for B (0 or 1): "))
C = int(input("Enter value for C (0 or 1): "))

result = compute_output(A, B, C)
print("Output Q =", result)
