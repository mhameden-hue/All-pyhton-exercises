# 1. INITIALIZATION: Create variable with start value 0
biggest = 0

# 2. LOOP: Repeat 5 times
for i in range(5):
    # 3. INPUT: Ask user for an integer
    number = int(input("Give a positive integer:\n"))

    # 4. EXTRA TASK: Check if number is positive
    if number > 0:
        # 5. COMPARISON: Check if number is larger than current biggest
        if number > biggest:
            biggest = number

# 6. OUTPUT: Print the largest given number
print(f"The biggest number was: {biggest}")