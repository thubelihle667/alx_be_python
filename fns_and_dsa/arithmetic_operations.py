def perform_operation(num1, num2, operation):
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (add, subtract, multiply, divide): ")

    match operation:
        case "add":
            result = num1 + num2
        case "subtract":
            result = num1 - num2    
        case "multiply":    
            result = num1 * num2
        case "divide":
            if num2 == 0:
                return "Error: Division by zero is not allowed."
            result = num1 / num2
        case _:
            return "Error: Invalid operation."
    return f"The result of {operation}ing {num1} and {num2} is: {result}"
if __name__ == "__main__":
    print(perform_operation())
