num1 = int(input("Enter the number 1 :"))
num2 = int(input("Enter the number 2 :"))

remainder = num1 % num2
while num1 > 0 and num2 < 100:
    if remainder == 0:
        print(num1, "is divisible by", num2)

    else:
        print(num1, "is not divisible by", num2)

    num1 = int(input("Enter the number 1 :"))
    num2 = int(input("Enter the number 2 :"))
