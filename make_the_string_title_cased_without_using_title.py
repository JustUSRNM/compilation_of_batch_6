# input a text
text= input('Please enter a text: ')
# split the text into words
words= text.split()
titled_words=[]
# in each word use .upper at the first letter and .lower to the rest
for individual_word in words:
    titled_words.append(individual_word[0].upper() + individual_word[1:])
# print the recombined words to make the text in title case
print (" ".join(titled_words))