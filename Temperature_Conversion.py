print("Select Scale To Convert From")

print("1. Celsius Scale")
print("2. Fahrenheit Scale")
print("3. Kelvin Scale")
print("4. Rankine Scale")
print("5. Delisle Scale")
print("6. Newton Scale")
print("7. Réaumur Scale")
print("8. Rømer Scale")
print("9. Exit")

choice = int(input("Enter the choice:"))

while choice > 0 and choice != 10:
    if choice == 1:
        print()
        print("Select Scale To Convert Into")
        print("1. To Fahrenheit Scale")
        print("2. To Kelvin Scale")
        print("3. To Rankine Scale")
        print("4. To Delisle Scale")
        print("5. To Newton Scale")
        print("6. To Réaumur Scale")
        print("7. To Rømer Scale")

        choice1 = int(input("Enter your Conversion Scale :"))

        if choice1 == 1:
            print("From Celcius to Fahrenheit")
            c = int(input("Enter the Temperature :"))
            f = c * 9 / 5 + 32
            print("So, your Temperature is", f, "Fahrenheit")
            print()

            print("Do you want to continue? Yes OR No")
            option = input("Enter your option :")
            if option == "Y" or "y":
                print()
                print("Select Scale To Convert From")
                print("1. Celsius Scale")
                print("2. Fahrenheit Scale")
                print("3. Kelvin Scale")
                print("4. Rankine Scale")
                print("5. Delisle Scale")
                print("6. Newton Scale")
                print("7. Réaumur Scale")
                print("8. Rømer Scale")
                print("9. Exit")

                choice = int(input("Enter the choice:"))

            if option == "N" or "n":
                print("Exit")
                break

        if choice1 == 2:
            print("From Celcius to Kelvin")
            c = int(input("Enter the Temperature :"))
            k = c + 273.15
            print("So, your Temperature is", k, "Kelvin")
            print()

            print("Do you want to continue? Yes OR No")
            option = input("Enter your option :")
            if option == "Y" or "y":
                print()
                print("Select Scale To Convert From")
                print("1. Celsius Scale")
                print("2. Fahrenheit Scale")
                print("3. Kelvin Scale")
                print("4. Rankine Scale")
                print("5. Delisle Scale")
                print("6. Newton Scale")
                print("7. Réaumur Scale")
                print("8. Rømer Scale")
                print("9. Exit")

                choice = int(input("Enter the choice:"))

            if option == "N" or "n":
                print("Exit")
                break

        if choice1 == 3:
            print("From Celcius to Rankine")
            c = int(input("Enter the Temperature :"))
            r = (c + 273.15) * 9 / 5
            print("So, your Temperature is", r, "Rankine")
            print()

        if choice1 == 4:
            print("From Celcius to Delisle")
            c = int(input("Enter the Temperature :"))
            de = (100 - c) * 3 / 2
            print("So, your Temperature is", de, "Delisle")
            print()

            print("Do you want to continue? Yes OR No")
            option = input("Enter your option :")
            if option == "Y" or "y":
                print()
                print("Select Scale To Convert From")
                print("1. Celsius Scale")
                print("2. Fahrenheit Scale")
                print("3. Kelvin Scale")
                print("4. Rankine Scale")
                print("5. Delisle Scale")
                print("6. Newton Scale")
                print("7. Réaumur Scale")
                print("8. Rømer Scale")
                print("9. Exit")

                choice = int(input("Enter the choice:"))

            if option == "N" or "n":
                print("Exit")
                break

        if choice1 == 5:
            print("From Celcius to Newton")
            c = int(input("Enter the Temperature :"))
            n = c * 33 / 100
            print("So, your Temperature is", n, "Newton")
            print()

            print("Do you want to continue? Yes OR No")
            option = input("Enter your option :")
            if option == "Y" or "y":
                print()
                print("Select Scale To Convert From")
                print("1. Celsius Scale")
                print("2. Fahrenheit Scale")
                print("3. Kelvin Scale")
                print("4. Rankine Scale")
                print("5. Delisle Scale")
                print("6. Newton Scale")
                print("7. Réaumur Scale")
                print("8. Rømer Scale")
                print("9. Exit")

                choice = int(input("Enter the choice:"))

            if option == "N" or "n":
                print("Exit")
                break

        if choice1 == 6:
            print("From Celcius to Réaumur")
            c = int(input("Enter the Temperature :"))
            re = c * 4 / 5
            print("So, your Temperature is", re, "Réaumur")
            print()

            print("Do you want to continue? Yes OR No")
            option = input("Enter your option :")
            if option == "Y" or "y":
                print()
                print("Select Scale To Convert From")
                print("1. Celsius Scale")
                print("2. Fahrenheit Scale")
                print("3. Kelvin Scale")
                print("4. Rankine Scale")
                print("5. Delisle Scale")
                print("6. Newton Scale")
                print("7. Réaumur Scale")
                print("8. Rømer Scale")
                print("9. Exit")

                choice = int(input("Enter the choice:"))

            if option == "N" or "n":
                print("Exit")
                break

        if choice1 == 7:
            print("From Celcius to Rømer")
            c = int(input("Enter the Temperature :"))
            ro = c * 21 / 40 + 7.5
            print("So, your Temperature is", ro, "Rømer")
            print()

            print("Do you want to continue? Y OR N")
            option = input("Enter your option :")
            if option == "Y":
                print()
                print("Select Scale To Convert From")
                print("1. Celsius Scale")
                print("2. Fahrenheit Scale")
                print("3. Kelvin Scale")
                print("4. Rankine Scale")
                print("5. Delisle Scale")
                print("6. Newton Scale")
                print("7. Réaumur Scale")
                print("8. Rømer Scale")
                print("9. Exit")

                choice = int(input("Enter the choice:"))

            if option == "N":
                print("Exit")
                break

            else:
                print("Enter Y OR N")

    if choice == 2:
        print()
        print("Select Scale To Convert Into")
        print("1. To Celcius Scale")
        print("2. To Kelvin Scale")
        print("3. To Rankine Scale")
        print("4. To Delisle Scale")
        print("5. To Newton Scale")
        print("6. To Réaumur Scale")
        print("7. To Rømer Scale")

        choice2 = int(input("Enter your Conversion Scale :"))

        if choice2 == 1:
            print("From Fahrenheit to Celcius")
            f = int(input("Enter the Temperature :"))
            c = (f - 32) * 5 / 9
            print("So, your Temperature is", c, "Celcius")
            print()

            print("Do you want to continue? Yes OR No")
            option = input("Enter your option :")
            if option == "Y" or "y":
                print()
                print("Select Scale To Convert From")
                print("1. Celsius Scale")
                print("2. Fahrenheit Scale")
                print("3. Kelvin Scale")
                print("4. Rankine Scale")
                print("5. Delisle Scale")
                print("6. Newton Scale")
                print("7. Réaumur Scale")
                print("8. Rømer Scale")
                print("9. Exit")

                choice = int(input("Enter the choice:"))

            if option == "N" or "n":
                print("Exit")
                break

        if choice2 == 2:
            print("From Fahrenheit to Kelvin")
            f = int(input("Enter the Temperature :"))
            k = (f + 459.67) * 5 / 9
            print("So, your Temperature is", k, "Kelvin")
            print()

            print("Do you want to continue? Yes OR No")
            option = input("Enter your option :")
            if option == "Y" or "y":
                print()
                print("Select Scale To Convert From")
                print("1. Celsius Scale")
                print("2. Fahrenheit Scale")
                print("3. Kelvin Scale")
                print("4. Rankine Scale")
                print("5. Delisle Scale")
                print("6. Newton Scale")
                print("7. Réaumur Scale")
                print("8. Rømer Scale")
                print("9. Exit")

                choice = int(input("Enter the choice:"))

            if option == "N" or "n":
                print("Exit")
                break

        if choice2 == 3:
            print("From Fahrenheit to Rankine")
            f = int(input("Enter the Temperature :"))
            r = f + 459.67
            print("So, your Temperature is", r, "Rankine")
            print()

            print("Do you want to continue? Yes OR No")
            option = input("Enter your option :")
            if option == "Y" or "y":
                print()
                print("Select Scale To Convert From")
                print("1. Celsius Scale")
                print("2. Fahrenheit Scale")
                print("3. Kelvin Scale")
                print("4. Rankine Scale")
                print("5. Delisle Scale")
                print("6. Newton Scale")
                print("7. Réaumur Scale")
                print("8. Rømer Scale")
                print("9. Exit")

                choice = int(input("Enter the choice:"))

            if option == "N" or "n":
                print("Exit")
                break

        if choice2 == 4:
            print("From Fahrenheit to Delisle")
            f = int(input("Enter the Temperature :"))
            de = (212 - f) * 5 / 6
            print("So, your Temperature is", de, "Delisle")
            print()

            print("Do you want to continue? Yes OR No")
            option = input("Enter your option :")
            if option == "Y" or "y":
                print()
                print("Select Scale To Convert From")
                print("1. Celsius Scale")
                print("2. Fahrenheit Scale")
                print("3. Kelvin Scale")
                print("4. Rankine Scale")
                print("5. Delisle Scale")
                print("6. Newton Scale")
                print("7. Réaumur Scale")
                print("8. Rømer Scale")
                print("9. Exit")

                choice = int(input("Enter the choice:"))

            if option == "N" or "n":
                print("Exit")
                break

        if choice2 == 5:
            print("From Fahrenheit to Newton")
            f = int(input("Enter the Temperature :"))
            n = (f - 32) * 11 / 60
            print("So, your Temperature is", n, "Newton")
            print()

            print("Do you want to continue? Yes OR No")
            option = input("Enter your option :")
            if option == "Y" or "y":
                print()
                print("Select Scale To Convert From")
                print("1. Celsius Scale")
                print("2. Fahrenheit Scale")
                print("3. Kelvin Scale")
                print("4. Rankine Scale")
                print("5. Delisle Scale")
                print("6. Newton Scale")
                print("7. Réaumur Scale")
                print("8. Rømer Scale")
                print("9. Exit")

                choice = int(input("Enter the choice:"))

            if option == "N" or "n":
                print("Exit")
                break

        if choice2 == 6:
            print("From Fahrenheit to Réaumur")
            f = int(input("Enter the Temperature :"))
            re = (f - 32) * 4 / 9
            print("So, your Temperature is", re, "Réaumur")
            print()

            print("Do you want to continue? Yes OR No")
            option = input("Enter your option :")
            if option == "Y" or "y":
                print()
                print("Select Scale To Convert From")
                print("1. Celsius Scale")
                print("2. Fahrenheit Scale")
                print("3. Kelvin Scale")
                print("4. Rankine Scale")
                print("5. Delisle Scale")
                print("6. Newton Scale")
                print("7. Réaumur Scale")
                print("8. Rømer Scale")
                print("9. Exit")

                choice = int(input("Enter the choice:"))

            if option == "N" or "n":
                print("Exit")
                break

        if choice2 == 7:
            print("From Fahrenheit to Rømer")
            f = int(input("Enter the Temperature :"))
            ro = (f - 32) * 7 / 24 + 7.5
            print("So, your Temperature is", ro, "Rømer")
            print()

            print("Do you want to continue? Yes OR No")
            option = input("Enter your option :")
            if option == "Y" or "y":
                print()
                print("Select Scale To Convert From")
                print("1. Celsius Scale")
                print("2. Fahrenheit Scale")
                print("3. Kelvin Scale")
                print("4. Rankine Scale")
                print("5. Delisle Scale")
                print("6. Newton Scale")
                print("7. Réaumur Scale")
                print("8. Rømer Scale")
                print("9. Exit")

                choice = int(input("Enter the choice:"))

            if option == "N" or "n":
                print("Exit")
                break

    if choice == 3:
        print()
        print("Select Scale To Convert Into")
        print("1. To Celcius Scale")
        print("2. To Fahrenheit Scale")
        print("3. To Rankine Scale")
        print("4. To Delisle Scale")
        print("5. To Newton Scale")
        print("6. To Réaumur Scale")
        print("7. To Rømer Scale")

        choice3 = int(input("Enter your Conversion Scale :"))

        if choice3 == 1:
            print("From Kelvin to Celcius")
            k = int(input("Enter the Temperature :"))
            c = k - 273.15
            print("So, your Temperature is", c, "Celcius")
            print()

            print("Do you want to continue? Yes OR No")
            option = input("Enter your option :")
            if option == "Y" or "y":
                print()
                print("Select Scale To Convert From")
                print("1. Celsius Scale")
                print("2. Fahrenheit Scale")
                print("3. Kelvin Scale")
                print("4. Rankine Scale")
                print("5. Delisle Scale")
                print("6. Newton Scale")
                print("7. Réaumur Scale")
                print("8. Rømer Scale")
                print("9. Exit")

                choice = int(input("Enter the choice:"))

            if option == "N" or "n":
                print("Exit")
                break

        if choice3 == 2:
            print("From Kelvin to Fahrenheit")
            k = int(input("Enter the Temperature :"))
            f = k * 9 / 5 - 459.67
            print("So, your Temperature is", f, "Fahrenheit")
            print()

            print("Do you want to continue? Yes OR No")
            option = input("Enter your option :")
            if option == "Y" or "y":
                print()
                print("Select Scale To Convert From")
                print("1. Celsius Scale")
                print("2. Fahrenheit Scale")
                print("3. Kelvin Scale")
                print("4. Rankine Scale")
                print("5. Delisle Scale")
                print("6. Newton Scale")
                print("7. Réaumur Scale")
                print("8. Rømer Scale")
                print("9. Exit")

                choice = int(input("Enter the choice:"))

            if option == "N" or "n":
                print("Exit")
                break

        if choice3 == 3:
            print("From Kelvin to Rankine")
            k = int(input("Enter the Temperature :"))
            r = k * 9 / 5
            print("So, your Temperature is", r, "Rankine")
            print()

            print("Do you want to continue? Yes OR No")
            option = input("Enter your option :")
            if option == "Y" or "y":
                print()
                print("Select Scale To Convert From")
                print("1. Celsius Scale")
                print("2. Fahrenheit Scale")
                print("3. Kelvin Scale")
                print("4. Rankine Scale")
                print("5. Delisle Scale")
                print("6. Newton Scale")
                print("7. Réaumur Scale")
                print("8. Rømer Scale")
                print("9. Exit")

                choice = int(input("Enter the choice:"))

            if option == "N" or "n":
                print("Exit")
                break

        if choice3 == 4:
            print("From Kelvin to Delisle")
            k = int(input("Enter the Temperature :"))
            de = (373.15 - k) * 3 / 2
            print("So, your Temperature is", de, "Delisle")
            print()

            print("Do you want to continue? Yes OR No")
            option = input("Enter your option :")
            if option == "Y" or "y":
                print()
                print("Select Scale To Convert From")
                print("1. Celsius Scale")
                print("2. Fahrenheit Scale")
                print("3. Kelvin Scale")
                print("4. Rankine Scale")
                print("5. Delisle Scale")
                print("6. Newton Scale")
                print("7. Réaumur Scale")
                print("8. Rømer Scale")
                print("9. Exit")

                choice = int(input("Enter the choice:"))

            if option == "N" or "n":
                print("Exit")
                break

        if choice3 == 5:
            print("From Kelvin to Newton")
            k = int(input("Enter the Temperature :"))
            n = (k - 273.15) * 33 / 100
            print("So, your Temperature is", n, "Newton")
            print()

            print("Do you want to continue? Yes OR No")
            option = input("Enter your option :")
            if option == "Y" or "y":
                print()
                print("Select Scale To Convert From")
                print("1. Celsius Scale")
                print("2. Fahrenheit Scale")
                print("3. Kelvin Scale")
                print("4. Rankine Scale")
                print("5. Delisle Scale")
                print("6. Newton Scale")
                print("7. Réaumur Scale")
                print("8. Rømer Scale")
                print("9. Exit")

                choice = int(input("Enter the choice:"))

            if option == "N" or "n":
                print("Exit")
                break

        if choice3 == 6:
            print("From Kelvin to Réaumur")
            k = int(input("Enter the Temperature :"))
            re = (k - 273.15) * 4 / 5
            print("So, your Temperature is", re, "Réaumur")
            print()

            print("Do you want to continue? Yes OR No")
            option = input("Enter your option :")
            if option == "Y" or "y":
                print()
                print("Select Scale To Convert From")
                print("1. Celsius Scale")
                print("2. Fahrenheit Scale")
                print("3. Kelvin Scale")
                print("4. Rankine Scale")
                print("5. Delisle Scale")
                print("6. Newton Scale")
                print("7. Réaumur Scale")
                print("8. Rømer Scale")
                print("9. Exit")

                choice = int(input("Enter the choice:"))

            if option == "N" or "n":
                print("Exit")
                break

        if choice3 == 7:
            print("From Kelvin to Rømer")
            k = int(input("Enter the Temperature :"))
            ro = (k - 273.15) * 21 / 40 + 7.5
            print("So, your Temperature is", ro, "Rømer")
            print()

            print("Do you want to continue? Yes OR No")
            option = input("Enter your option :")
            if option == "Y" or "y":
                print()
                print("Select Scale To Convert From")
                print("1. Celsius Scale")
                print("2. Fahrenheit Scale")
                print("3. Kelvin Scale")
                print("4. Rankine Scale")
                print("5. Delisle Scale")
                print("6. Newton Scale")
                print("7. Réaumur Scale")
                print("8. Rømer Scale")
                print("9. Exit")

                choice = int(input("Enter the choice:"))

            if option == "N" or "n":
                print("Exit")
                break

    if choice == 4:
        print()
        print("Select Scale To Convert Into")
        print("1. To Celcius Scale")
        print("2. To Fahrenheit Scale")
        print("3. To Kelvin Scale")
        print("4. To Delisle Scale")
        print("5. To Newton Scale")
        print("6. To Réaumur Scale")
        print("7. To Rømer Scale")

        choice4 = int(input("Enter your Conversion Scale :"))

        if choice4 == 1:
            print("From Rankine to Celcius")
            r = int(input("Enter the Temperature :"))
            c = (r - 491.67) * 5 / 9
            print("So, your Temperature is", c, "Celcius")
            print()

            print("Do you want to continue? Yes OR No")
            option = input("Enter your option :")
            if option == "Y" or "y":
                print()
                print("Select Scale To Convert From")
                print("1. Celsius Scale")
                print("2. Fahrenheit Scale")
                print("3. Kelvin Scale")
                print("4. Rankine Scale")
                print("5. Delisle Scale")
                print("6. Newton Scale")
                print("7. Réaumur Scale")
                print("8. Rømer Scale")
                print("9. Exit")

                choice = int(input("Enter the choice:"))

            if option == "N" or "n":
                print("Exit")
                break

        if choice4 == 2:
            print("From Rankine to Fahrenheit")
            r = int(input("Enter the Temperature :"))
            f = r - 459.67
            print("So, your Temperature is", f, "Fahrenheit")
            print()

            print("Do you want to continue? Yes OR No")
            option = input("Enter your option :")
            if option == "Y" or "y":
                print()
                print("Select Scale To Convert From")
                print("1. Celsius Scale")
                print("2. Fahrenheit Scale")
                print("3. Kelvin Scale")
                print("4. Rankine Scale")
                print("5. Delisle Scale")
                print("6. Newton Scale")
                print("7. Réaumur Scale")
                print("8. Rømer Scale")
                print("9. Exit")

                choice = int(input("Enter the choice:"))

            if option == "N" or "n":
                print("Exit")
                break

        if choice4 == 3:
            print("From Rankine to Kelvin")
            r = int(input("Enter the Temperature :"))
            k = r * 5 / 9
            print("So, your Temperature is", k, "Kelvin")
            print()

            print("Do you want to continue? Yes OR No")
            option = input("Enter your option :")
            if option == "Y" or "y":
                print()
                print("Select Scale To Convert From")
                print("1. Celsius Scale")
                print("2. Fahrenheit Scale")
                print("3. Kelvin Scale")
                print("4. Rankine Scale")
                print("5. Delisle Scale")
                print("6. Newton Scale")
                print("7. Réaumur Scale")
                print("8. Rømer Scale")
                print("9. Exit")

                choice = int(input("Enter the choice:"))

            if option == "N" or "n":
                print("Exit")
                break

        if choice4 == 4:
            print("From Rankine to Delisle")
            r = int(input("Enter the Temperature :"))
            de = (671.67 - r) * 5 / 6
            print("So, your Temperature is", de, "Delisle")
            print()

            print("Do you want to continue? Yes OR No")
            option = input("Enter your option :")
            if option == "Y" or "y":
                print()
                print("Select Scale To Convert From")
                print("1. Celsius Scale")
                print("2. Fahrenheit Scale")
                print("3. Kelvin Scale")
                print("4. Rankine Scale")
                print("5. Delisle Scale")
                print("6. Newton Scale")
                print("7. Réaumur Scale")
                print("8. Rømer Scale")
                print("9. Exit")

                choice = int(input("Enter the choice:"))

            if option == "N" or "n":
                print("Exit")
                break

        if choice4 == 5:
            print("From Rankine to Newton")
            r = int(input("Enter the Temperature :"))
            n = (r - 491.67) * 11 / 60
            print("So, your Temperature is", n, "Newton")
            print()

            print("Do you want to continue? Yes OR No")
            option = input("Enter your option :")
            if option == "Y" or "y":
                print()
                print("Select Scale To Convert From")
                print("1. Celsius Scale")
                print("2. Fahrenheit Scale")
                print("3. Kelvin Scale")
                print("4. Rankine Scale")
                print("5. Delisle Scale")
                print("6. Newton Scale")
                print("7. Réaumur Scale")
                print("8. Rømer Scale")
                print("9. Exit")

                choice = int(input("Enter the choice:"))

            if option == "N" or "n":
                print("Exit")
                break

        if choice4 == 6:
            print("From Rankine to Réaumur")
            r = int(input("Enter the Temperature :"))
            re = (r - 491.67) * 4 / 9
            print("So, your Temperature is", re, "Réaumur")
            print()

            print("Do you want to continue? Yes OR No")
            option = input("Enter your option :")
            if option == "Y" or "y":
                print()
                print("Select Scale To Convert From")
                print("1. Celsius Scale")
                print("2. Fahrenheit Scale")
                print("3. Kelvin Scale")
                print("4. Rankine Scale")
                print("5. Delisle Scale")
                print("6. Newton Scale")
                print("7. Réaumur Scale")
                print("8. Rømer Scale")
                print("9. Exit")

                choice = int(input("Enter the choice:"))

            if option == "N" or "n":
                print("Exit")
                break

        if choice4 == 7:
            print("From Rankine to Rømer")
            r = int(input("Enter the Temperature :"))
            ro = (r - 491.67) * 7 / 24 + 7.5
            print("So, your Temperature is", ro, "Rømer")
            print()

            print("Do you want to continue? Yes OR No")
            option = input("Enter your option :")
            if option == "Y" or "y":
                print()
                print("Select Scale To Convert From")
                print("1. Celsius Scale")
                print("2. Fahrenheit Scale")
                print("3. Kelvin Scale")
                print("4. Rankine Scale")
                print("5. Delisle Scale")
                print("6. Newton Scale")
                print("7. Réaumur Scale")
                print("8. Rømer Scale")
                print("9. Exit")

                choice = int(input("Enter the choice:"))

            if option == "N" or "n":
                print("Exit")
                break


    else:
        print()
        print("Select Scale To Convert into")
        print("1. Celsius Scale")
        print("2. Fahrenheit Scale")
        print("3. Kelvin Scale")
        print("4. Rankine Scale")
        print("5. Delisle Scale")
        print("6. Newton Scale")
        print("7. Réaumur Scale")
        print("8. Rømer Scale")
        print("9. Exit")

        choice = int(input("Enter the choice:"))
