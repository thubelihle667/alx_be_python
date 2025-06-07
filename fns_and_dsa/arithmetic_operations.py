def perform_operation(num1, num2, operation):
    if operation == "add":
        result = num1 + num2
    elif operation == "subtract":
        result = num1 - num2
    elif operation == "multiply":
        result = num1 * num2
    elif operation == "divide":
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        else:
            result = num1 / num2
    else:
        return "Error: Invalid operation."

    return f"The result of {operation}ing {num1} and {num2} is: {result}"


if __name__ == "__main__":
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (add, subtract, multiply, divide): ")
    print(perform_operation(num1, num2, operation))
