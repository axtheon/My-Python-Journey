a = {1, 2, 3} # it is the syntax of a set.
# As both Dictionary and Set uses same brackets,
# most people get confused between an empty Set and an empty Dictionary
# Don't use b = {} as it will create an empty dictionary.
b = set() # it is an empty set.
# This concept is a common question in interviews.
# They ask a question like: Make an empty set.
print(a)
print(type(b))
c = {} # It is empty Dictionary
print(type(c))
# we can't repeat any element in a set.
d = {1, 2, 93, 64, 55, 2, 2, 2, 1}
print(d)
# A set doesn't maintain the order, it output the values randomly.