# To find the double spaces in a string.
name = "Abdullah Saeed Khan"
print(name.find("  "))
# this will output -1 because there are no double spaces in the string.
name = "Abdullah  Saeed  Khan"
print(name.find("  "))
# this will output 8 because there are double spaces in the string.

# The find() method returns the lowest index of the substring if found in given string.
# If not found, it returns -1.
name = "Abdullah Saeed Khan"
print(name.find("eed"))
# this will output 11 because the index eed starts at 11 in the string. 