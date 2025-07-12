"""
Functions, lambda, and type inspection print examples.
"""

def square(x):
    """Return square of x."""
    return x * x

def run():
    print("\n-- Function Call Expression --")
    print("square(5) ->", square(5))

    print("\n-- Type Expressions --")
    print("type(10)    ->", type(10))
    print("type('Hi')  ->", type("Hi"))
    print("type([])    ->", type([]))

if __name__ == "__main__":
    run()
