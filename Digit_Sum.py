num = int(input("Enter the number: "))
Sum = 0

while num > 0:
    Reminder = num % 10
    Sum = Sum + Reminder
    num = num // 10

print("Sum of the digits of Given Number =%d" % Sum)
