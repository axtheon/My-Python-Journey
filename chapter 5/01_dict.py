# A dictionary is same as a list but if you want that
# key values should associate with each other you can
# use a list.
marks = {
    "Abdullah": 100,
    "Ali": 84,
    "Ahmed": 26
}
print(marks, type(marks))
# In dictionaries, we cant use indexing to print a single value
# we have to use the name of the key.
# Like if you want to print marks of Ali:
print("Marks of Ali are: ", + marks["Ali"])
# Properties of Dictionaries:
# They are mutable
# They are unordered
# They are already indexed in the code means it will not go through all
# The values in it instead it will directly go to the value we want to
# print. So it's faster than lists, tuples etc.
# They cannot contain duplicate keys.
