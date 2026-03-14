def convert_units(conversion_type, value):
    """
    Convert a value between different units of measurement.

    Parameters:
    conversion_type (int): The selected conversion option.
        1 = meters to feet
        2 = feet to meters
        3 = kilograms to pounds
        4 = pounds to kilograms
        5 = liters to gallons
        6 = gallons to liters

    value (float): The numeric value that needs to be converted.

    Returns:
    float: The converted value based on the selected conversion type.
    """

    if conversion_type == 1:
        return value * 3.28084
    elif conversion_type == 2:
        return value / 3.28084
    elif conversion_type == 3:
        return value * 2.20462
    elif conversion_type == 4:
        return value / 2.20462
    elif conversion_type == 5:
        return value * 0.264172
    elif conversion_type == 6:
        return value / 0.264172
    else:
        return None


def main():
    print("Unit Conversion Program")
    print("\nSelect conversion type:")
    print("1. Meters to Feet")
    print("2. Feet to Meters")
    print("3. Kilograms to Pounds")
    print("4. Pounds to Kilograms")
    print("5. Liters to Gallons")
    print("6. Gallons to Liters")

    try:
        choice = int(input("\nEnter conversion option (1-6): "))
        if choice not in range(1, 7):
            print("Error: Unsupported conversion type.")
            return

        value = float(input("Enter the value to convert: "))

        result = convert_units(choice, value)

        if result is None:
            print("Conversion failed.")
        else:
            print(f"Converted value: {result:.4f}")

    except ValueError:
        print("Error: Please enter a valid numeric value.")


if __name__ == "__main__":
    main()