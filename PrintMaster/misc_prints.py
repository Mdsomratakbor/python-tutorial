"""
Miscellaneous examples: bitwise, math library, boolean casting.
"""


import math

def run():
    print("\n-- Bitwise Expressions --")
    print("5 & 3  ->", 5 & 3)
    print("5 | 3  ->", 5 | 3)
    print("5 ^ 3  ->", 5 ^ 3)
    print("~5     ->", ~5)
    print("5 << 1 ->", 5 << 1)
    print("5 >> 1 ->", 5 >> 1)

    print("\n-- Math Library Expressions --")
    print("math.sqrt(16)     ->", math.sqrt(16))
    print("math.pow(2,3)     ->", math.pow(2, 3))
    print("math.factorial(5) ->", math.factorial(5))

    print("\n-- Boolean Casting --")
    name = "samrat"
    print("bool(0)    ->", bool(0))
    print("bool(1)    ->", bool(1))
    print("bool('')   ->", bool(''))
    print("bool('Hi') ->", bool('Hi'))
    print("Name is empty or not empty check ->", bool(name))
if __name__ == "__main__":
    run()

