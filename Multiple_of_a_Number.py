# Prompt the user to enter five numbers
print("Enter the five numbers:")

# Get user input for the five numbers and the divisor
num1 = float(input("First Number: "))
num2 = float(input("Second Number: "))
num3 = float(input("Third Number: "))
num4 = float(input("Fourth Number: "))
num5 = float(input("Fifth Number: "))
divisor = float(input("Enter divisor Number: "))

# Initialize a counter for multiples
count = 0

# Print multiples of the divisor
print("Multiples of", divisor, "are:")

# Check if each number is a multiple of the divisor
remainder = num1 % divisor
if remainder == 0:
    print(num1, sep="")
    count += 1

remainder = num2 % divisor
if remainder == 0:
    print(num2, sep="")
    count += 1

remainder = num3 % divisor
if remainder == 0:
    print(num3, sep="")
    count += 1

remainder = num4 % divisor
if remainder == 0:
    print(num4, sep="")
    count += 1

remainder = num5 % divisor
if remainder == 0:
    print(num5, sep="")
    count += 1

# Print the total number of multiples found
print()
print(count, "multiples of", divisor, "found")
