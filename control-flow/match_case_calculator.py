
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation_type = input("Choose the operation (+, -, *, /): ")

match operations:
    case "+":
        result = num1 + num2
        print(f"The result is {result}.")

    case "-":
        result = num1 - num2
        print(f"The result is {result}.")

    case "*":
        result = num1 * num2
        print(f"The result is {result}.")
        
    case "/":
        if num2 == 0:
            print(f"Cannot divide by zero.")
        else:
            result = num1 / num2
            print(f"The result is {result}.")

    case _:
        print("Invalid entry, please try again.")

