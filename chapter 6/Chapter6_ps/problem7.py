# Write a program that finds out, if the post is talkingg about Abdullah or not.
post = input("Enter the post: ")

if "abdullah" in post.lower():
    print("This post is talking about Abdullah.")
else:
    print("This post is not talking about Abdullah.")
