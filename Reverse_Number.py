# Take an integer input from the user
num = int(input("Enter the Number: "))

# Initialize a variable to store the reversed number
rev = 0

# Reverse the digits using a while loop
while num > 0:
    rem = num % 10         # Get the last digit of num
    rev = (rev * 10) + rem  # Append the last digit to rev (reversed number)
    num = num // 10        # Remove the last digit from num

# Print the reversed number
print("Reverse of entered number is = %d" % rev)
