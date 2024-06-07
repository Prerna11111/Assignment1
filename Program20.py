#How can you remove specific characters from a string in Python?

#removepreffix() and removesuffix() method use to remove first and last character from string

var1 = "We Are one of the best technical team "
string1 = var1.removeprefix("We")
string2 = var1.removesuffix("team ")
print(string1)
print(string2)