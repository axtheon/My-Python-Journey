# Create an empty dictionary, Allow 4 friends to enter their
# favorite language as value and use their names as the keys.
# Suppose that each name is different.
d = {}

name = input("Enter your name: ")
lang = input("Enter your language: ")
d.update({name: lang})
name = input("Enter your name: ")
lang = input("Enter your language: ")
d.update({name: lang})
name = input("Enter your name: ")
lang = input("Enter your language: ")
d.update({name: lang})
name = input("Enter your name: ")
lang = input("Enter your language: ")
d.update({name: lang})

print(d)