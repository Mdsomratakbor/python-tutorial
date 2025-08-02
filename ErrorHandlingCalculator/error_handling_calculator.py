def calculator(num1, num2, operator):
    try: 
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            result = num1 / num2  # May raise ZeroDivisionError
        else:
            raise ValueError("Unsupported operator. Use +, -, *, or /.")
    except ZeroDivisionError:
        print('Error Cannot divide by zero.')
    except ValueError as ve:
        print(f'Error: {ve}')
    else:
        print(f'Result: {result}')
    finally:
        print("Calculation attempt completed.\n")