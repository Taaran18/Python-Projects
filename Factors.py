# Get user input for a number
num = int(input("Enter the number: "))

# Check if the number is greater than 0
if num > 0:
    count = 0
    number = int(num)

    # Loop to find factors
    for i in range(2, number):
        if number % i == 0:
            print(i)
            count += 1

    # Check if any factors were found
    if count == 0:
        print(number, "is a prime number.")
    else:
        print(number, "is not a prime number.")

else:
    print(num, "has no factors because it is not a positive number.")
