# Get a floating-point number from the user
num = float(input("Enter the number :"))

# Iterate through numbers from 1 to 100 (inclusive)
for a in range(1, 101):
    # Print the multiplication table for the entered number
    print(num, "x", a, "=", num * a)
