# ask for shipment type (l = letter, p = parcel)
shipment_type =input("Letter or parcel (l/p):\n")

# ask for weight in grams
weight = int(input("Weight in grams:\n"))

# calculate base cost and extra rate per 100g
if shipment_type == "l":
    total_cost=0.50
    if weight<=200:
        extra_rate=0
    elif 500<=weight:
        extra_rate=0.07
    else:
     extra_rate=0.05
if shipment_type=="p":
    total_cost=2
    if weight<=200:
        extra_rate=0
    elif 500<=weight:
      extra_rate=0.08
    else:
     extra_rate=0.14
# calculate extra cost based on full 100g
full_100g = weight // 100
total_cost = total_cost + (full_100g *extra_rate)

# special condition for letter over 500g
if shipment_type == "l" and weight > 500:
    fits = input("Does the letter fit the mailbox (y/n):\n")
    if fits == "n":
        total_cost = total_cost + 2.00

# print the final price rounded to 2 decimal places
print(f"Postage fee: {round(total_cost, 2)},$")
