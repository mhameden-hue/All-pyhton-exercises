text = "The quick brown fox jumps over the lazy dog. That \
sentence contains every letter in the English alphabet. Neat!"
print(text)
#replace word fox with duck
text=text.replace('fox','dock')
print(text)
# remove the word from text
word=input('which word should be removed:\n')
if word in text:
    text = text.replace(word, "")
    print(text)
else:
    print('word not found')
#number of characters
text_length = len(text)
print(text_length)
#number of characters
word_count = len(text.split())
print(f"{word_count} words.")
#delet dots and start new lins insted
delet_dots=text.replace('.',"\n")
print(delet_dots)