num = int(input("Enter the Number :"))
fact = 1
if num <= 0:
    print("The Factorial of 0 is 1.")
else:
    for i in range(1, num + 1):
        fact = fact * i
    print("The factorial of", num, "is", fact)
