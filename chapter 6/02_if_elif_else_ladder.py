# if, elif, else ladder:

age = int(input("Enter your age: "))

if age >= 18:
    print("You are above the age of consent.")

elif age >= 1:
    print("You are below the age of consent.")

elif age == 0:
    print("Dont Joke with me :)")

else:
    print("Invalid age.")
