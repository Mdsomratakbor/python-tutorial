def view_profile():
    print("Profile Details...")

def edit_profile():
    print("Edit your profile here...")

def logout():
    print("Logging out...")

def default():
    print("Invalid options.")

def run():
    print("\n-- Using dictionary as switch --")
    
    options = {
        "1": view_profile,
        "2": edit_profile,
        "3": logout
    }
    
    choice = input("Choose an option (1-3): ")
    action = options.get(choice, default)
    action()