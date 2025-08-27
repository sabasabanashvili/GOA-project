def division_calculator():
    try:
        numerator = float(input("Enter the numerator: "))
        denominator = float(input("Enter the denominator: "))

        if denominator == 0:
            raise ValueError("You cannot divide by zero!")

        result = numerator / denominator
        print("Result:", result)

    except ValueError as ve:
        print("ValueError:", ve)

    except Exception as e:
        print("Invalid input. Please enter numeric values.")

    finally:
        print("Operation complete.")

# Run the calculator
division_calculator()
