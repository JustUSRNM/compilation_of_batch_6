# input a word with starting spaces
word= input('Please enter a word with mutiple starting spaces:')
# count the number of starting spaces
number_of_spaces= 0
while word[number_of_spaces] == " ":
    number_of_spaces += 1
# remove the starting spaces
word_no_spaces= word[number_of_spaces:]
# print inputted word without the starting spaces
print (word_no_spaces)