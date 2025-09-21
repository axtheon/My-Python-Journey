# Write a program to find out that a student is pass or fail.

from curses import tparm


marks1 = int(input("Enter marks of subject 1: "))
marks2 = int(input("Enter marks of subject 2: "))
marks3 = int(input("Enter marks of subject 3: "))

total_percentage = (100 * (marks1 + marks2 + marks3)) / 300

if total_percentage >= 40 and marks1 >= 33 and marks2 >= 33 and marks3 >= 33:
    print("You are pass. Your percentage is: ",total_percentage)
else:
    print("You are fail! Your percentage is: ",total_percentage)

