"""
Loop‑related print examples.
"""


def run():
    print("\n-- For Loop Example --")
    for i in range(10):
        print(f"i = {i}")
    
    print("\n-- List Comprehension + print --")
    my_list = [10, 520, 30]
    [print(x) for x in my_list ]

    print("\n-- Conditional (Ternary) Expression --")
    x = 10
    print("Even" if x % 2 == 0 else "Odd")
    
if __name__ == "__main__":
    run()