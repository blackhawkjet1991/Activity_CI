import calculator


def get_user_input(user_input):
    values = user_input.split()
    if len(values) != 2:
        raise ValueError("Exactly 2 values should be provided.")
    return tuple(map(int, values))


def main(user_selection, user_input):
    try:
        selection = int(user_selection)

        if selection not in [1, 2, 3, 4]:
            raise ValueError("Invalid selection. Please choose a number from 1 to 4.")

        num1, num2 = get_user_input(user_input)

        if selection == 1:
            result = calculator.add(num1, num2)
            print("Result:", result)
        elif selection == 2:
            result = calculator.subtract(num1, num2)
            print("Result:", result)
        elif selection == 3:
            result = calculator.multiply(num1, num2)
            print("Result:", result)
        elif selection == 4:
            try:
                result = calculator.divide(num1, num2)
                print("Result:", result)
            except ValueError as e:
                print("Error:", str(e))

    except ValueError as e:
        print("Error:", str(e))

# Get user input and call the main function
if __name__ == "__main__":
    selection_input = input("\nSelect your calculator operation:"
                            "\n1. Addition"
                            "\n2. Subtraction"
                            "\n3. Multiplication"
                            "\n4. Division\n")

    values_input = input("\nProvide your 2 values separated by space: ")

    main(selection_input, values_input)

