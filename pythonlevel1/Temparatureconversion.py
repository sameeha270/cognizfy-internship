# Temperature Conversion Program with loop and basic validation

while True:
    try:
        temp_value = float(input("Enter the temperature value: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    unit_type = input("Enter the unit (C for Celsius, F for Fahrenheit): ")
    unit_type = unit_type.upper()

    if unit_type == "C":
        converted_temp = (temp_value * 9/5) + 32
        print("Converted Temperature:", round(converted_temp, 2), "°F")

    elif unit_type == "F":
        converted_temp = (temp_value - 32) * 5/9
        print("Converted Temperature:", round(converted_temp, 2), "°C")

    else:
        print("Invalid unit entered. Please enter C or F.")
        continue

    # asking user if they want to continue
    choice = input("Do you want to convert another temperature? (yes/no): ")
    if choice.lower() != "yes":
        print("Program ended.")
        break