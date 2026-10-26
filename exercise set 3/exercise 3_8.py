# ask total price
total_price = float(input("Total price of purchases:\n"))

# ask student status
is_student = input("Are you a student (y/n):\n")

# ask vip status
is_vip = input("Are you a VIP-client (y/n):\n")

# initial vip points
vip_points = 0

# get vip points if vip client
if is_vip == "y":
    vip_points = int(input("How many VIP-points do you have:\n"))

# ask for sales code
has_code = input("Do you have a discount code (y/n):\n")

# check sales code
if has_code == "y":
    code = input("Enter discount code:\n")
    if code == "FALL26":
        total_price = total_price * 0.90
    if code == "BK2SCHOOL":
        if is_student == "y":
            total_price = total_price * 0.80

# add new vip points from purchase (100 points per 10 euro)
if is_vip == "y":
    new_points = int(total_price // 10) * 100
    vip_points = vip_points + new_points

# reduce 5 euro per 1000 total vip points
if is_vip == "y":
    total_price = total_price - (vip_points // 1000) * 5

# add postage cost
if total_price < 99:
    total_price = total_price + 7.95

# print total result
print(f"Final price: {round(total_price, 2)}€")