def run():
    print("\n-- Boolean Input and Casting --")

    response = input("Do you want to continue? (yes/no): ").strip().lower()

    is_yes = response in ['yes','y','true','1']

    print("Interpreted as:", is_yes)
    print("Type:", type(is_yes))