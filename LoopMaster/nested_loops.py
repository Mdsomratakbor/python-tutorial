def run():
    print("\n-- Nested Loops --")
    
    for i in range(1, 10):
        for j in range(i+1, 10):
            print(f"{i} x {j} = {i * j}")
    print("---")