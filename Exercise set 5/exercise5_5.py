# 1.CREATE TUPLE: Store the names of all 12 months
months = (
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"
)

# USER INPUT: Ask the user for the month number (1-12)
month_number = int(input("Give the number of month:\n"))

# OUTPUT: Subtract 1 from the input to match the 0-based index and print
print(months[month_number - 1])