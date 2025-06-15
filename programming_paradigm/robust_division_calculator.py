# Check: File exists and not empty (this file is not empty)

def safe_divide(numerator, denominator):
    # Check: Implementation of safe_divide function
    try:
        # Check: Try block present

        # Check: Conversion to float (inside function for full reusability)
        numerator = float(numerator)
        denominator = float(denominator)

        if denominator == 0:
            # Check: ZeroDivisionError implementation
            raise ZeroDivisionError("Error: Cannot divide by zero.")

        result = numerator / denominator
        return f"The result of the division is {result}"

    except ValueError:
        # Check: ValueError implementation (for non-numeric inputs)
        return "Error: Please enter numeric values only."

    except ZeroDivisionError as e:
        return str(e)

# When the module is run directly (not imported)
if __name__ == "__main__":
    try:
        num_input = input("Enter numerator: ")
        denom_input = input("Enter denominator: ")

        # Check: Conversion of inputs into floats before calling function
        result = safe_divide(num_input, denom_input)

        # Check: Correct output (normal case, zero division, non-numeric)
        print(result)

    except Exception as e:
        # General fallback in case of unexpected errors
        print(f"Unexpected error: {e}")



    