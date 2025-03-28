# input a word and the width parameter of ljust
word= input('Please enter a word: ')
parameter= int(input('Enter what width the word be in: '))
# width subtracted to the length of the word, is how many spaces are added
if parameter > len(word):
    spaces= parameter - len(word)
elif parameter <= len(word):
    spaces = 0
# print the word in the given width
print (word+ spaces*" ")