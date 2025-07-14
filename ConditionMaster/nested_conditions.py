def run():
    print('\n-- Nested Conditions --')

    score = 85
    if(score>=33):
        print("Passed")
        if(score>=80):
            print("A+")
        elif(score>=70):
            print("A")
        elif(score>=60):
            print("A-")
        else:
            print("B")
    else:
        print("Failed")
        