# Get user input for the first and second numbers
num1 = int(input("Enter the 1st number : "))
num2 = int(input("Enter the 2nd number : "))

# Calculate the remainder of the division
remainder = num1 % num2

# Check conditions and enter the loop
while num1 > 0 and num2 < 100:
    # Check if num1 is divisible by num2
    if remainder == 0:
        print(num1, "is divisible by", num2)
    else:
        print(num1, "is not divisible by", num2)

    # Get user input for the next iteration
    num1 = int(input("Enter the 1st number : "))
    num2 = int(input("Enter the 2nd number : "))

    # Calculate the remainder for the next iteration
    remainder = num1 % num2
