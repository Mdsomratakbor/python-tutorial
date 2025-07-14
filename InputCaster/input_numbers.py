def run():
    print("\n-- Number Input and Type Casting --")
    
    age_input = input("Enter your age: ")
    age = int(age_input)  # Convert string to int
    print(f"You are {age} years old.")
    print("Type of age:", type(age))
    
    height_input = input("Enter your height in meters: ")
    height = float(height_input)  # Convert string to float
    print(f"Your height is {height} meters.")
    print("Type of height:", type(height))
