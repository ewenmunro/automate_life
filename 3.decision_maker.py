from random import choice

# ask user to input options
options_str = input("Enter a list of options, separated by commas: ")

# replace any additional whitespace characters with a single space
options_str = " ".join(options_str.split())

# split options by comma
options = options_str.split(",")

# capitalize options that begin with a word
capitalized_options = []
for option in options:
    if option[0].isalpha():
        capitalized_options.append(option.strip().capitalize())
    else:
        capitalized_options.append(option.strip())

# print result
print(f"{choice(capitalized_options)}")
