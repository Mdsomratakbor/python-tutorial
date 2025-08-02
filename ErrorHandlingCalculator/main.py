import error_handling_calculator as ehc

def run():
    while True:
        print("Simple Calculator (type 'exit' to stop)\n")
        try:
            first = input("Enter first number: ")
            if first.lower == 'exit':
                break
            
            num1 = float(first)
            second = input("Enter second number: ")
            
        except ValueError:
            print("Invalid input ! Please enter numeric values. \n")