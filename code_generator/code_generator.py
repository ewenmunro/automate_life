import random
import string

# Define the length of the code
length = 24

# Define the possible characters for the code
characters = string.ascii_letters + string.digits + '!@#$%&*?'

# Generate the code
code = ''.join(random.choice(characters) for i in range(length))

# Print the code
print(code)
