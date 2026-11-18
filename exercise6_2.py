# 1. MAIN LOOP: Keep running the application until the user stops it
while True:
    # 2. USER INPUT: Ask which multiplication table to print (0 stops)
    table = int(input("Which multiplication table would you like to see? (1-10). 0 stops program.\n"))

    # 3. EXIT CONDITION: Stop the loop if user enters 0
    if table == 0:
        break

    # 4. VALIDATION & MULTIPLICATION LOOP: Check if number is in range 1-10
    elif 1 <= table <= 10:
        for i in range(1, 11):
            print(f"{table} * {i} = {table * i}")

    # 5. INVALID INPUT: Inform the user if the number is outside 1-10
    else:
        print("Wrong number format.")

# 6. EXIT MESSAGE: Print final message after the loop ends
print("Thank you for using the application!")