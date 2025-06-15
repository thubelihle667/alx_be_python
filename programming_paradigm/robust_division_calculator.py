
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

    except ( ValueError, ZeroDivisionError) as e:
        return(f"{e}")



if __name__ == "__main__":
    safe_divide() 


    