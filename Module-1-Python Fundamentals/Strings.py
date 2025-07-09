
# Sequence Data Types
# String
s ="Hello Amar" # can be '' used or '''Hello ........  ''' triple quotes (''' or """) can be used
print("S = ", s);
print(type(s));

# Accessing string 
print("first character",s[0]) #first character
print("last character",s[9]) #last character
#Negative indexing
# H e l l o   A m a r
# 0 1 2 3 4 5 6 7 8 9
#-10-9-8-7-6-5-4-3-2-1
print("last character",s[-1]) #last character
print("first character",s[-10]) #first character

# String Slicing
# s: The original string.
# start (optional): Starting index (inclusive). Defaults to 0 if omitted.
# end (optional): Stopping index (exclusive). Defaults to the end of the string if omitted.
# substring = s[start : end : step]
# Retrieves characters from index 1 to 3
print(s[1:4])  

# Retrieves characters from beginning to index 2
print(s[:3])   

# Retrieves characters from index 3 to the end
print(s[3:])   

# Reverse a string
print(s[::-1])

# PYTHON STRINGS ARE IMMUTABLE : they cannot be changed after they are created
#  methods like concatenation, slicing, or formatting are used to create new strings based on the original.

# s ="Hello Amar"
s1 = "A" + s[1:]; #Replace first letter of S with "A"
print("S1 = > ", s1);

s2 = s.replace("Amar", "Yash")#Replacing Amar with Yash
print("S2", s2);

# COMMON STRING METHODS
print(len(s)); # length - returns total no of characters in string
print(s.upper())#//convert all characters to UpperCase
print(s.lower())#//convert all characters to LowerCase
# s2 = s.replace(old, new)
print(s.strip())  # Removes leading and trailing WhiteSpaces

# Concat strings using + operator
s4 = s2 + " " + s1;
print("S4 ", s4);

# repeat string using * operator
s5 = s4 * 3;
print("S5 ", s5);

# Check for substring using in
print("Amar" in s) # returns bool
print("Kunal" in s) # returns bool
# CHANGING CASE
# lower(): Converts all characters in the string to lowercase.
# capitalize(): Capitalizes the first character of the string and makes the rest lowercase.
# title(): Capitalizes the first letter of each word in the string.
# swapcase(): Swap the cases of all characters in a string
# capitalize(): Convert the first character of a string to uppercase







