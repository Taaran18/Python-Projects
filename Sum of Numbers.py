num = int(input("Enter the number :"))
sum = 0

while num > 0:
    sum = sum + num
    num = int(input("Enter the number :"))

    if num == 0 or num < 0:
        print("The sum is :", sum)
