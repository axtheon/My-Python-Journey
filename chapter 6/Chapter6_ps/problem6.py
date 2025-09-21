# Write a program to find the grade of the student with respect to their percentage.
sub1 = int(input("Enter the marks of Mathematics: "))
sub2 = int(input("Enter the marks of Physics: "))
sub3 = int(input("Enter the marks of Chemistry: "))
sub4 = int(input("Enter the marks of English: "))
sub5 = int(input("Enter the marks of Computer: "))

percentage = (100 * (sub1 + sub2 + sub3 + sub4 + sub5)) / 500

if percentage >= 90:
        print("You have got A+ grade with: ",percentage, "percent.")
elif 80 <= percentage < 90:
        print("You have got A grade with: ",percentage, "percent.")
elif 70 <= percentage < 80:
        print("You have got B+ grade with: ",percentage, "percent.")
elif 60 <= percentage < 70:
        print("You have got B grade with: ",percentage, "percent.")
elif 50 <= percentage < 60:
        print("You have got C grade with: ",percentage, "percent.")
elif 40 <= percentage < 50:
        print("You have got D grade with: ",percentage, "percent.")
elif 33 <= percentage < 40:
        print("You have got E grade with: ",percentage, "percent.")
else:
        print("You are fail with ",percentage, "percent.")
