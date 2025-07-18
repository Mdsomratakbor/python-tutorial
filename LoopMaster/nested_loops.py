def run():
    print("\n-- Nested Loops --")
    
    for i in range(1, 10):
        for j in range(i+1, 10):
            print(f"{i} x {j} = {i * j}")
    print("---")
    
def print_X():
    for item in [3, 9, 2, 1, 4, 5, 6, 1]:
        output = ''
        for digit in range(item):
            output += 'X'
        print(output)