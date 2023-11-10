print("Enter the five numbers :")

num1 = float(input("First Number :"))
num2 = float(input("Second Number :"))
num3 = float(input("Third Number :"))
num4 = float(input("Fourth Number :"))
num5 = float(input("Fifth Number :"))
divisor = float(input("Enter divisor Number :"))

count = 0
print("Multiples of", divisor, "are :")

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

print()
print(count, "multiples of", divisor, "found")
