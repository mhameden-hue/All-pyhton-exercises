import math
# Get inputs from the user
a = float(input("Enter value for a: "))
b = float(input("Enter value for b: "))
c = float(input("Enter value for c: "))
# Calculate the discriminant (b^2 - 4ac)
discriminant = b**2 - 4 * a * c
# Calculate the square root of discriminant
sqrt_val = math.sqrt(discriminant)
# Calculate x1 and x2
x1 = (-b + sqrt_val) / (2 * a)
x2 = (-b - sqrt_val) / (2 * a)
# Print the results
print("x1 =", x1)
print("x2 =", x2)