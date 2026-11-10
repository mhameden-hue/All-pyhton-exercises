# give money
money = int(input("Give money:\n"))

# purchase cost
cost = int(input("Purchase cost:\n"))

# check conditions
if money == cost:
    print("Thank you for your purchase!")

elif money > cost:
    # calculate change
    change = money - cost
    print("Thank you. Here's the change: {change} $")

else:
    # calculate missing money
    needed_money = cost - money

    # ask for more money
    more_money = int(input(f"Not enough money, please give {needed_money} more:\n"))
    money = money + more_money

    # check conditions again
    if money == cost:
        print("Thank you for your purchase!")
    elif money > cost:
        # calculate change
        change = money - cost
        print("Thank you. Here's the change: {change} $")
    else:
        print("You don't have enough money.")
