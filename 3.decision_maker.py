from random import choice

# ask user to input options
options = input("Enter a list of options, separated by commas: ").split(",")

# print result
print(choice(options))
