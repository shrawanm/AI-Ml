def find_sum(numbers):
    """
    Calculate the sum of a list of numbers.

    Parameters:
    numbers (list): A list of numeric values.

    Returns:
    float: The sum of all numbers in the list.
    """
    return sum(numbers)


def find_average(numbers):
    """
    Calculate the average of a list of numbers.

    Parameters:
    numbers (list): A list of numeric values.

    Returns:
    float: The average of the numbers.
    """
    return sum(numbers) / len(numbers)


def find_max(numbers):
    """
    Find the maximum value in a list of numbers.

    Parameters:
    numbers (list): A list of numeric values.

    Returns:
    float: The largest number in the list.
    """
    return max(numbers)


def find_min(numbers):
    """
    Find the minimum value in a list of numbers.

    Parameters:
    numbers (list): A list of numeric values.

    Returns:
    float: The smallest number in the list.
    """
    return min(numbers)


def main():
    print("Mathematical Operations on a List")
    print("1. Sum")
    print("2. Average")
    print("3. Maximum")
    print("4. Minimum")

    try:
        choice = int(input("Choose an operation (1-4): "))
        numbers_input = input("Enter numbers separated by spaces: ")
        numbers = [float(num) for num in numbers_input.split()]

        if len(numbers) == 0:
            print("Error: The list cannot be empty.")
            return
        if choice == 1:
            result = find_sum(numbers)
            print("Sum:", result)
        elif choice == 2:
            result = find_average(numbers)
            print("Average:", result)
        elif choice == 3:
            result = find_max(numbers)
            print("Maximum:", result)
        elif choice == 4:
            result = find_min(numbers)
            print("Minimum:", result)
        else:
            print("Invalid operation selected.")
    except ValueError:
        print("Error: Please enter valid numeric values.")
if __name__ == "__main__":
    main()