# Detecting Double Spaces in a String
str1 = "Python is a programming language  that lets you work quickly and integrate systems more effectively."

print(str1.find("  "))

# Output:  32 (index of the first occurrence of double space) 
# If there is no double space, it will return -1
# We can only find the first occurrence using this method

# Replacing double spaces with single spaces

print(str1 + "\n") # Lets print Original string First 

print(str1.replace("  ", " ") + "\n") # Replacing double space with single space and printing the modified string