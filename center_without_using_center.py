# input a word then the length parameter
word= input('Please enter a word: ')
parameter= int(input('Enter how much spaces do you want the word be centered in: '))
# using arithmetic to get the how many padding is need on both sides
total_spaces = parameter - len(word)
left_spaces = total_spaces // 2
right_spaces = total_spaces - left_spaces
# print the word centered by the parameter
print (" "*left_spaces + word + " "*right_spaces)