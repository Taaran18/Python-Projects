def celsius_to_other_scales(celsius, scale):
    if scale == 1:
        return celsius * 9 / 5 + 32  # Celsius to Fahrenheit
    elif scale == 2:
        return celsius + 273.15  # Celsius to Kelvin
    elif scale == 3:
        return (celsius + 273.15) * 9 / 5  # Celsius to Rankine
    elif scale == 4:
        return (100 - celsius) * 3 / 2  # Celsius to Delisle
    elif scale == 5:
        return celsius * 33 / 100  # Celsius to Newton
    elif scale == 6:
        return celsius * 4 / 5  # Celsius to Réaumur
    elif scale == 7:
        return celsius * 21 / 40 + 7.5  # Celsius to Rømer


def fahrenheit_to_other_scales(fahrenheit, scale):
    if scale == 1:
        return (fahrenheit - 32) * 5 / 9  # Fahrenheit to Celsius
    elif scale == 2:
        return (fahrenheit + 459.67) * 5 / 9  # Fahrenheit to Kelvin
    elif scale == 3:
        return fahrenheit + 459.67  # Fahrenheit to Rankine
    elif scale == 4:
        return (212 - fahrenheit) * 5 / 6  # Fahrenheit to Delisle
    elif scale == 5:
        return (fahrenheit - 32) * 11 / 60  # Fahrenheit to Newton
    elif scale == 6:
        return (fahrenheit - 32) * 4 / 9  # Fahrenheit to Réaumur
    elif scale == 7:
        return (fahrenheit - 32) * 7 / 24 + 7.5  # Fahrenheit to Rømer


def kelvin_to_other_scales(kelvin, scale):
    if scale == 1:
        return kelvin - 273.15  # Kelvin to Celsius
    elif scale == 2:
        return kelvin * 9 / 5 - 459.67  # Kelvin to Fahrenheit
    elif scale == 3:
        return kelvin * 9 / 5  # Kelvin to Rankine
    elif scale == 4:
        return (373.15 - kelvin) * 3 / 2  # Kelvin to Delisle
    elif scale == 5:
        return (kelvin - 273.15) * 33 / 100  # Kelvin to Newton
    elif scale == 6:
        return (kelvin - 273.15) * 4 / 5  # Kelvin to Réaumur
    elif scale == 7:
        return (kelvin - 273.15) * 21 / 40 + 7.5  # Kelvin to Rømer


def rankine_to_other_scales(rankine, scale):
    if scale == 1:
        return (rankine - 491.67) * 5 / 9  # Rankine to Celsius
    elif scale == 2:
        return rankine - 459.67  # Rankine to Fahrenheit
    elif scale == 3:
        return rankine * 5 / 9  # Rankine to Kelvin
    elif scale == 4:
        return (671.67 - rankine) * 5 / 6  # Rankine to Delisle
    elif scale == 5:
        return (rankine - 491.67) * 11 / 60  # Rankine to Newton
    elif scale == 6:
        return (rankine - 491.67) * 4 / 9  # Rankine to Réaumur
    elif scale == 7:
        return (rankine - 491.67) * 7 / 24 + 7.5  # Rankine to Rømer


while True:
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

    if choice == 9:
        print("Exit")
        break

    if choice in range(1, 9):
        print("Select Scale To Convert Into")
        print("1. To Celsius Scale")
        print("2. To Fahrenheit Scale")
        print("3. To Kelvin Scale")
        print("4. To Rankine Scale")
        print("5. To Delisle Scale")
        print("6. To Newton Scale")
        print("7. To Réaumur Scale")
        print("8. To Rømer Scale")

        choice_conversion = int(input("Enter your Conversion Scale :"))

        temperature_input = float(input("Enter the Temperature :"))

        if choice == 1:
            result = celsius_to_other_scales(temperature_input, choice_conversion)
        elif choice == 2:
            result = fahrenheit_to_other_scales(temperature_input, choice_conversion)
        elif choice == 3:
            result = kelvin_to_other_scales(temperature_input, choice_conversion)
        elif choice == 4:
            result = rankine_to_other_scales(temperature_input, choice_conversion)

        print(f"Result: {result:.2f}")
    else:
        print("Invalid Choice! Please enter a valid choice.")
