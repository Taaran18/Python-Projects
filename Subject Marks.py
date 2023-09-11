marks = int(input("Enter your marks :"))

if marks >= 90:
    print("Grade A")
    per = (marks / 100) * 100
    print(per)

if 80 <= marks < 90:
    print("Grade B")
    per = (marks / 100) * 100
    print(per)

if 70 <= marks < 80:
    print("Grade C")
    per = (marks / 100) * 100
    print(per)

if 60 <= marks < 70:
    print("Grade D")
    per = (marks / 100) * 100
    print(per)

if 50 <= marks < 60:
    print("Grade E")
    per = (marks / 100) * 100
    print(per)

else:
    print("FAIL")
