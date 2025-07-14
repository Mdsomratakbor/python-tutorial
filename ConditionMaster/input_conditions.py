def run():
    print("\n-- Input-based Conditions --")
    
    name = input("Enter your name: ")
    
    if name:
        print(f"Hello, {name}")
    else:
        print("You didn't enter a name!")
    
    
    num = int(input("Enter a number: "))
    
    if num > 0:
        print("Positive")
    elif num == 0:
        print("Zero")
    else:
        print("Negative")