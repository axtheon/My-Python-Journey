# Write a program that finds weather a given name has less than 10 characters or not.
name = input("Enter your name: ")

if (len(name) < 10):
    print("Your name has less than 10 characters.")
else:
    print("Your name has 10 or more characters.")
