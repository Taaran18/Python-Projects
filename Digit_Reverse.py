# Get user input for a number
num = int(input("Enter number:"))

# Initialize variables for reverse and temporary storage
rev = 0
original_num = num

# Reverse the digits of the number
while num > 0:
    dig = num % 10
    rev = rev * 10 + dig
    num = num // 10

# Check if the original number is equal to its reverse
if original_num == rev:
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")
