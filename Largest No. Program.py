x = y = z = 0

x = float(input("Enter the First Number :"))
y = float(input("Enter the Second Number :"))
z = float(input("Enter the Third Number :"))

max = x
if y > max:
    max = y

if z > max:
    max = z

print("Largest Number is :", max)
