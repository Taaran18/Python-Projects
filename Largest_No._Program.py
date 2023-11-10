# Initialize variables for x, y, z
x = y = z = 0

# Get user input for three numbers
x = float(input("Enter the First Number: "))
y = float(input("Enter the Second Number: "))
z = float(input("Enter the Third Number: "))

# Assume x is the largest initially
max = x

# Check if y is greater than the current max
if y > max:
    max = y

# Check if z is greater than the current max
if z > max:
    max = z

# Print the largest number
print("Largest Number is:", max)
