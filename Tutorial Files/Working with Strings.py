name = "justin"

print("\"Hello\nWorld\"")
# \n makes the text coming after it go to a new line
# to add " or ' in a string, add a \ before it

print("His name is " + name + ".")
# to append a variable to a string, use "+"

print(len(name))
# len is used to check the length of a string, spaces inclusive

print(name.upper())
# upper() and lower() can be use to change a whole string to either upper or lower case respectively

print(name.islower())
# isupper() and islower() can be used to check if the string is either all upper or lower case respectively
# and return True or False

print(name[0])
# prints character at specified index starting with 0, so the above would print "j"

print(name.index("j"))
# finds index(es) with letter specified, above code would print "0"
# if letter not found, error would be returned

print(name.replace("justin", "jordan"))
# replace certain phrases with other specified phrases

# to check more things you can do with string, check out:
# https://www.w3schools.com/python/python_strings.asp
