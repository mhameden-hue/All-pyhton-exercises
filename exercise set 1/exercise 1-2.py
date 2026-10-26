# This initializes the variable "price" by asking input from user and
# then converts the input to a float
price=float(input('give the price without vat:\n'))
#vat
vat=1.255
#price_with_vat
price_with_vat=round(price*vat,2)

print("price with vat=",price_with_vat,'$')

