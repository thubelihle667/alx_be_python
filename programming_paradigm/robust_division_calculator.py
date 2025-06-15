def safe_divide(numerator, denominator):
    try:
        if not isinstance(numerator, (int, float)):
            raise ValueError("Error: Please enter numeric values only.")
        elif not isinstance(denominator, (int, float)):
            raise ValueError("Error: Please enter numeric values only.")
        elif denominator == 0:
            raise ZeroDivisionError("Error: Cannot divide by zero.")

        result = numerator / denominator
        return f"The result of the division is {result}"

    except (ValueError, ZeroDivisionError) as e:
        return str(e)
    
if __name__ == "__main__":
    try:
        num_input = input("Enter numerator: ")
        denom_input = input("Enter denominator: ")

        numerator = float(num_input)
        denominator = float(denom_input)

        result = safe_divide(numerator, denominator)
        print(result)

    except ValueError:
        print("Error: Please enter numeric values only.")


    