# start value for special price
special_price = False

# ask for student status and travel month
is_student = input("Are you a student? (y/n)\n")
month = int(input("Travel month? (1-12)\n"))

# check if student
if is_student == "y":
    special_price = True

# check if summer month (6 to 8)
if 6 <= month <= 8:
    special_price = False

# print result based on special_price
if special_price:
    print("Special price!")
else:
    print("Normal price.")