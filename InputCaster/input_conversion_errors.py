def run():
    print("\n-- Handling Input Conversion Errors --")

    user_input = input("Enter a number: ")
    
    try:
        number = int(user_input)
        print("Converted to integer:", number)
    except ValueError:
        print("❌ Invalid integer input!")

    try:
        number = float(user_input)
        print("Converted to float:", number)
    except ValueError:
        print("❌ Invalid float input!")
