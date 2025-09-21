# if statements can be used multiple times
# but else statements cannot be used multiple times.

age = int(input("Enter your age: "))

# if statement NO:1
if age%2 ==0:
    print("Age is even")

# if statement NO:2
if age >= 18:
    print("You are above the age of consent.")

elif age >= 1:
    print("You are below the age of consent.")

elif age == 0:
    print("Dont Joke with me :)")

else:
    print("Invalid age.")