# Initialize variables for sum1 and sum2
sum1 = sum2 = 0

# Get user input for three numbers
num1 = int(input("Enter the number 1: "))
num2 = int(input("Enter the number 2: "))
num3 = int(input("Enter the number 3: "))

# Calculate the sum of the three given numbers
sum1 = num1 + num2 + num3

# Check for duplicate numbers
if num1 == num2:
    if num3 != num1:
        # If num1 and num2 are equal but num3 is different, add num3 to sum2
        sum2 += num3
else:
    if num1 == num3:
        # If num1 and num3 are equal, add num2 to sum2
        sum2 += num2
    else:
        if num2 != num3:
            # If num1, num2, and num3 are all different, add num1 to sum2
            sum2 += num1
        else:
            # If num1, num2, and num3 are all equal, add their sum to sum2
            sum2 += num1 + num2 + num3

# Print the numbers and sums
print("Numbers are", num1, num2, num3)
print("Sum of three given numbers is:", sum1)
print("Sum of non-duplicate number is:", sum2)
