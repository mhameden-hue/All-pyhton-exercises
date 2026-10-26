# 1. Start with try: to monitor these lines for errors
try:
    first_num = int(input("First number:\n"))
    second_num = int(input("Second number:\n"))
    print(first_num / second_num)

# 2.text input errors
except ValueError:
    print("Incorrect format.")

# 3.division by zero errors
except ZeroDivisionError:
    print("You can't divide by zero.")