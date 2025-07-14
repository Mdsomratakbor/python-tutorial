def run():
    print("-- Using if-elseif-else (classic switch alternative)--")
   
    choice = input("Choose an option (1-3): ")
    
    if choice == "1":
        print("You chose option 1: View Profile")
    elif choice == "2":
        print("You chose option 2: Edit Profile")
    elif choice == "3":
        print("You chose option 3: Logout")
    else:
        print("Invalid option.")