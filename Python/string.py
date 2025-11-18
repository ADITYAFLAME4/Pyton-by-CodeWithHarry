# We can primarily write a string in these three ways. 

# Single quoted string 
a ='akash'       
# Double quoted string 
b = "akash"      
# Triple quoted string
c = '''akash'''  


# STRING SLICING - A string in python can be sliced for getting a part of the strings.


# Example:1
short_string = a[0:3]  # This will get characters from index 0 to index 2 (3 is excluded)
print(short_string)  # Output: aka
# Example:2
short_string = b[1:5]  # This will get characters from index 1 to index 4 (5 is excluded)
print(short_string)  # Output: kash

# Negative Indexing in String Slicing: we can also use negative indexing to slice strings.

# Example:3
short_string = c[-5:-1]  # This will get characters from index -5 to index -2 (-1 is excluded)
print(short_string)  # Output: kash
# here -1 refers to the last character, -2 to the second last character and so on, in negative indexing -1 refers to the last character of the string.

# Some weird yet advanced examples of String Slicing:
# Example:4
short_string = a[:]  # This will get the whole string
print(short_string)  # Output: akash

short_string = b[::2]  # This will get every second character of the string
print(short_string)  # Output: aks

short_string = c[::-1]  # This will reverse the string
print(short_string)  # Output: hsaka    
# Here, the slice [::-1] means to take the whole string but with a step of -1, effectively reversing it.

short_string = a[1:] # This will get the string from index 1 to the end, empty after colon means go till end (or length of string), It basically means [1:5] in this case as per the string given.
print(short_string)  # Output: kash 

short_string = b[:4] # This will get the string from start to index 3, empty before colon means start from 0, It basically means [0:4] in this case as per the string given.
print(short_string)  # Output: akas

# Note: String slicing creates a new string and does not modify the original string, as strings in Python are immutable.


# SLICING WITH SKIP VALUE - The syntax for slicing with skip value is [start:end:step], where 'step' is the skip value.
# We can provide a skip value as a part of our slice like this: 

d = "Hello, World!"

skip_string = d[0:9:2]  # This will get every second character from index 0 to index 8
print(skip_string)  # Output: Hlo

skip_string = d[2:13:4]  # This will get every fourth character from index 2 to index 12
print(skip_string)  # Output: l r

skip_string = d[2:11:2] # This will get every second character from index 2 to index 10
print(skip_string)  # Output: lo o

skip_string = d[::-2]  # This will get every second character in reverse order
print(skip_string)  # Output: !lo olH