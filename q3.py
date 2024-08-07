# String Manipulation

# Task: Given the string s, use string methods to:
# Capitalize the first letter: make the first character uppercase and the rest of the string lowercase.
# Convert to uppercase: change all characters in the string to uppercase.
# Convert to lowercase: change all characters in the string to lowercase.
# s:str = "hElLo WoRlD"
# Expected Output:
# Hello world
# HELLO WORLD
# hello world


# Given string
s:str = "hElLo WoRlD"

# Capitalize the first letter and make the rest lowercase
capitalized = s.capitalize()

# Convert all characters to uppercase
uppercase = s.upper()

# Convert all characters to lowercase
lowercase = s.lower()

# Printing the results
print(capitalized)
print(uppercase)
print(lowercase)
