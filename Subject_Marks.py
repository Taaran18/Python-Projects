# Get input from the user
marks = int(input("Enter your marks: "))

# Check the grade based on the marks
if marks >= 90:
    print("Grade A")
elif 80 <= marks < 90:
    print("Grade B")
elif 70 <= marks < 80:
    print("Grade C")
elif 60 <= marks < 70:
    print("Grade D")
elif 50 <= marks < 60:
    print("Grade E")
else:
    print("FAIL")

# Calculate percentage
per = (marks / 100) * 100

# Print the calculated percentage
print("Percentage:", per)
