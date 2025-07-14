def run():
    print("\n-- Loop Control: break and continue --")
    
    print("Break at 3:")
    
    for i in range(5):
        if i == 3:
            break
        print(i)
        
    print("Continue at 3:")
    for i in range(5):
        if i == 3:
            continue
        print(i)
        
    print("Loop with else:")
    for i in range(3):
        print("Looping", i)
    else:
        print("Loop ended normally (no break)")