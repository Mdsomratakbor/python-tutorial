def run():
    print("\n-- String Formatting --")
    name = "Alice"
    age = 30
    email="alice@gmail.com"

    print(f"My name is {name} and I am {age} Years old.")
    print("Using format():{} is {} years old and email is {}.".format(name, age, email))

    items = ["Apple", "Banana", "Cherry"]
    print("Joined list with comma:",",".join(items))
