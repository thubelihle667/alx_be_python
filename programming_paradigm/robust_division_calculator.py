

def safe_divide(numerator, denominator):
    
    try:
        numerator = float(numerator)
        denominator = float(denominator)

        if denominator == 0:
            raise ZeroDivisionError("Error: Cannot divide by zero.")

        result = numerator / denominator
        return f"The result of the division is {result}"

    except ValueError:
        return "Error: Please enter numeric values only."

    except ZeroDivisionError as e:
        return str(e)

if __name__ == "__main__":
    try:
        num_input = input("Enter numerator: ")
        denom_input = input("Enter denominator: ")
        result = safe_divide(num_input, denom_input)
        print(result)

    except Exception as e:

        print(f"Unexpected error: {e}")



    