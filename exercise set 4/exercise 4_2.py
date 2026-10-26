# ask user for a text
text = input("Give some text:\n")

# reverse the given text (save to a separate variable)
reversed_text = text[::-1]

# check if text is empty or palindrome
if text == "":
    print("Your text is empty.")
elif text == reversed_text:
    print(reversed_text)
    print("Palindrome: YES")
else:
    print(reversed_text)
    print("Palindrome: NO")
