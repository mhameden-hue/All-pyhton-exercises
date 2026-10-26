# set boolean variables to False
freezing = False
heatwave = False
raining = False
hailstorm = False

# ask temperature and humidity from user
temp = int(input("Temperature:\n"))
humidity = int(input("Humidity percentage:\n"))

# check temperature conditions
if temp < 0:
    freezing = True

if temp > 20:
    heatwave = True

# check humidity conditions
if humidity > 80:
    if temp < -20:
        hailstorm = True
    else:
        raining = True

# print temperature first
print(f"Temperature: {temp}")

# print freezing message
if freezing:
    print("It's freezing outside.")

# print rain or hailstorm message
if hailstorm:
    print("There's a hailstorm, be careful!")
elif raining:
    print("It's raining.")

# print heatwave message
if raining and heatwave:
    print("It's damp and hot")
elif heatwave:
    print("Heatwave! Remember to hydrate!")