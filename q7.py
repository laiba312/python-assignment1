# String Stripping and Justifying
# Task: Given the string s, use string methods to:
# Remove leading/trailing spaces: remove all leading and trailing whitespace characters from the string.
# Left justify with '*': left justify the string within a field of width 20, using * as the fill character.
# Right justify with '*': right justify the string within a field of width 20, using * as the fill character.
# s:str ="   Python is fun!   "
# Expected Output:
# Python is fun!
# Python is fun!*****
# *****Python is fun!



# Given string
s:str = "   Python is fun!   "

# Remove leading/trailing spaces
trimmed_string = s.strip()

# Left justify with '*'
left_justified = trimmed_string.ljust(20, '*')

# Right justify with '*'
right_justified = trimmed_string.rjust(20, '*')

# Printing the results
print(trimmed_string)
print(left_justified)
print(right_justified)
