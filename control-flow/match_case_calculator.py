num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the secodf number: "))
sign = input("Choose the operation (+, -, *, /): ")

match sign:
    case '+':
        result = num1 + num2
        print(f"The result is {result}.")
    case '-':
        result = num1 - num2
        print(f"The result is {result}.")
    case '*':
        result = num1 * num2
        print(f"The result is {result}.")
    case '/':
        if num2 != 0:
            result = num1 / num2
            print(f"The result is {result}.")
        else:
            print("Cannot divide by zero.")
    case _: 
        print("Invalid operation. Please choose from +, -, *, /.")
