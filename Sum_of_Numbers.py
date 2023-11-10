# Initialize the sum variable
sum = 0

# Get the first number from the user
num = int(input("Enter the number :"))

# Continue taking input until the user enters 0 or a negative number
while num > 0:
    # Add the current number to the sum
    sum = sum + num

    # Get the next number from the user
    num = int(input("Enter the number :"))

    # Check if the entered number is 0 or negative, then print the sum
    if num == 0 or num < 0:
        print("The sum is:", sum)
