def run():
    print("\n-- Shorthand (Ternary) Conditions --")
    age = 17
    
    result = "Adult" if age>= 18 else "Minor"
    print(f"You are a:{result}")
    
    number = 8
    even_odd = "Even" if number % 2 == 0 else "Odd"
    print(f"{number} is {even_odd}")