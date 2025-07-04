# What will be the length
s = set()
s.add(20)
s.add(20.0) # As 20.0 == 20 and set considers many repeating
# values as one single value so it will not be counted.
# that's why the answer will be 2.
s.add("20")
print(len(s))

# For Example:
a = 20 == 20.0
print(a)
# the answer will be true while both data types are different but
# the numerical value is same. so python determine it numerically.