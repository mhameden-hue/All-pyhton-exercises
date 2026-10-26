

cents = int(input("How many cents(1-100):\n"))


coin50 = cents // 50
cents = cents % 50

coin20 = cents // 20
cents = cents % 20

coin10 = cents // 10
cents = cents % 10


coin5 = cents // 5
cents = cents % 5


coin2 = cents // 2
cents = cents % 2


coin1 = cents


print("50 Cents:", coin50)
print("20 Cents:", coin20)
print("10 Cents:", coin10)
print("5 Cents:", coin5)
print("2 Cents:", coin2)
print("1 Cents:", coin1)