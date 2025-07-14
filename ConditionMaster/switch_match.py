def run():
    print("\n-- Using match-case (Python 3.10+) --")

    choice = input("Choose an option (1-3): ")
    
    match choice:
        case "1":
            print("You selected: View Profile")
        case "2":
            print("You selected: Edit Profile")
        case "3":
            print("You selected: Logout")
        case _:
            print("Invalid option.")