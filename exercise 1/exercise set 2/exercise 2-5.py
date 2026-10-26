import random
# a) Generate a random number between 1 and 10
num = random.randint(1, 10)
print("Random number:", num)
# b) Generate two side lengths between 2 and 10
side1 = random.randint(2, 10)
side2 = random.randint(2, 10)
# Calculate area
area = side1 * side2
# Print the sides and area on separate lines
print("First random side:", side1)
print("Second random side:", side2)
print("Rectangle area:", area)