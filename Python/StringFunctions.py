# Quick Summary (Most Used)
'''
.len()
.lower() .upper()
.strip()
.split() .join()
.find() .replace()
.startswith() .endswith()
f-strings
.count()
'''

# len() - Returns the length of a string.

len("hello")  # 5

# .islower(), .isupper() Check letter case.

"hello".islower()  # True
"HELLO".isupper()  # True

# .isalpha(), .isdigit(), .isalnum(), .isspace() - Check if the string contains only letters [ .isalpha() ], digits [ .isdigit() ], alphanumeric [ .isalnum() ], or spaces [ .isspace() ].

"abc".isalpha()  # True
"123".isdigit()  # True
"abc123".isalnum()  # True
"   ".isspace()  # True

#Case Conversion-  .lower(), .upper() - Convert case.

"Hello".lower()  # "hello"
"Hello".upper()  # "HELLO"

# .title(), .capitalize()

"hello world".title()       # "Hello World"
"hello world".capitalize()  # "Hello world"

# .swapcase()

"HeLLo".swapcase()  # "hEllO"

#Searching-  .find() - Returns first index or `-1`.

"hello".find("l")  # 2 Explanation: The first occurrence of the substring "l" is at index 2 in the string "hello".

# .index() - Like find, but errors on failure.

"hello".index("l")  # 2

# .startswith(), .endswith()

"hello".startswith("he")  # True
"hello".endswith("lo")    # True

#Slicing & Modifying -       .strip(), .lstrip(), .rstrip()    - Remove whitespace (or specified characters).

"  hi  ".strip()  # "hi"

# .replace()

"hello world".replace("world", "Python")  # "hello Python"  , It will change all occurrences of "world" with "Python".


#Splitting & Joining -  .split() - Split by delimiter (default: whitespace).

"a,b,c".split(",")  # ["a", "b", "c"]

# .rsplit() -Split from the right.

"a,b,c".rsplit(",", 1)  # ["a,b", "c"]

# .join() - Join a list into a string.

",".join(["a", "b", "c"])  # "a,b,c"



#Formatting  .format()

"Hello {}".format("world")


# f-strings (most common modern way of formatting)

name = "Alex"
f"Hello {name}"
# Output: "Hello Alex"


# .center(), .ljust(), .rjust()

"hi".center(6, "-")  # "--hi--" Explanation: Total width is 6, "hi" takes 2 spaces, so 4 dashes are added, 2 on each side.
"hi".ljust(6, "-")   # "hi----" Explanation: Total width is 6, "hi" takes 2 spaces, so 4 dashes are added to the right.
"hi".rjust(6, "-")   # "----hi" Explanation: Total width is 6, "hi" takes 2 spaces, so 4 dashes are added to the left.

#Character Work -    ord() , chr()

ord('A')  # 65
chr(65)   # 'A'



# Useful Less-Known Methods -     .startswith() / .endswith()  / .zfill() - For file extensions, prefixes, etc.

"filename.txt".endswith(".txt")  # True
"document.pdf".startswith("doc")  # True
"42".zfill(5)  # "00042" Explanation: The string "42" is padded with leading zeros to make its total length 5.


# .partition() / .rpartition() -    Split into a tuple (before, separator, after).

"key=value".partition("=")  # ("key", "=", "value") Explanation: The string is split at the first occurrence of "=", 
#resulting in a tuple with three elements: the part before the separator, the separator itself, and the part after the separator.

"key=value".rpartition("=")  # ("key", "=", "value") Explanation: The string is split at the last occurrence of "=", 
#resulting in a tuple with three elements: the part before the separator, the separator itself, and the part after the separator.

# .count() - Count occurrences of a substring.  
"hello world".count("o")  # 2

 

