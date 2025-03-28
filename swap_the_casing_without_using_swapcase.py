# input a word
word= input('Please enter a word: ')
# using for loop, check each character then switch they're casing with upper and lower
swapped_word=""
for char in word:
    if 'a' <= char <= 'z':
        swapped_word += char.upper()
    elif 'A' <= char <= 'Z':
        swapped_word += char.lower()
    else:
        swapped_word += char
# print the word with it's casing swapped
print (swapped_word)