import math

# Step 1: Calculate cherry
cherry = 2 + 2 * 2 + 2 - 2 - 2

# Step 2: Calculate apple
part1 = math.sqrt(3 + 10 - 4) / 3
part2 = (5 * 5 * 5 - 5) / 20
apple = part1 + part2 + 3

# Step 3: Calculate other fruits
orange = apple - 9
banana = cherry - 10
pear = banana - 8

# Step 4: The last picture has pear + cherry together
pear_cherry = pear + cherry

# Step 5: Final calculation
result = apple - banana + (orange * pear_cherry)

# Print values of each fruit
print("Cherry:", int(cherry))
print("Apple:", int(apple))
print("Orange:", int(orange))
print("Banana:", int(banana))
print("Pear:", int(pear))

# Print final result
print("Final Result:", int(result))