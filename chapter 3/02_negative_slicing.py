name = "ABDULLAH"
print(name[0:5])

print(name[-4: -1])
print(name[4:7])

print(name[:4]) # it is same as print(name[0:4])
print(name[1:]) # it is same as print(name[1:7])
print(name[1:5])
# there is no need to do negative slicing but its useful for interviews

# slicing with skip value
word = "0123456789"
a = word[1: 6: 2] # this will start from the digit 1 and end at 5. means first of all the [1:6] part will be executed. then it will execute the 2 part. so it will start from 1 and then skip 2 digits and so on. like that it will output 135.
print(a)