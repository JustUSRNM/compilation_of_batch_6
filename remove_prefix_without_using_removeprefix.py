# input a word and then the prefix
word= input('Please enter a word: ')
parameter= input('Please enter a prefix that is in the word: ')
# check if the prefix is in the inputted word
if word.startswith(parameter):
# get the len of prefix and remove it from the word
    no_prefix= word[len(parameter):]
# print the word without the prefix
    print (no_prefix)