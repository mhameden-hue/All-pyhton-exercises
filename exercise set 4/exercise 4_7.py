# ask for input from user
user_input = input("Give numbers or words:\n")

# check if the input is numeric (numbers to words)
if user_input.isnumeric():
    if len(user_input) <= 5:
        result = user_input
        result = result.replace("0", "zero ")
        result = result.replace("1", "one ")
        result = result.replace("2", "two ")
        result = result.replace("3", "three ")
        result = result.replace("4", "four ")
        result = result.replace("5", "five ")
        result = result.replace("6", "six ")
        result = result.replace("7", "seven ")
        result = result.replace("8", "eight ")
        result = result.replace("9", "nine ")
        print(result.strip())
    else:
        print("Maximum 5 numbers allowed.")

# if input is text (words to numbers)
else:
    result = user_input
    result = result.replace("zero", "0")
    result = result.replace("one", "1")
    result = result.replace("two", "2")
    result = result.replace("three", "3")
    result = result.replace("four", "4")
    result = result.replace("five", "5")
    result = result.replace("six", "6")
    result = result.replace("seven", "7")
    result = result.replace("eight", "8")
    result = result.replace("nine", "9")
    result = result.replace(" ", "")
    print(result)