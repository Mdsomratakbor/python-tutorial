"""
List, tuple, set and dictionary print examples.
"""

def run():
    print("\n-- List Expressions --")
    my_list = [1, 2, 3]
    print("my_list ->", my_list)
    print("my_list[0] ->", my_list[0])
    print("my_list + [4,5] ->", my_list + [4, 5])
    print("my_list * 2 ->", my_list * 4)
    print("len(my_list) ->", len(my_list))

    print("\n-- Tuple Expressions --")
    my_tuple = (1, 2, 3)
    print("my_tuple ->", my_tuple)
    print("my_tuple[1] ->", my_tuple[1])

    print("\n-- Set Expressions --")
    my_set = {1, 2, 3}
    print("my_set ->", my_set)
    print("2 in my_set ->", 2 in my_set)
    print("my_set | {3,4} ->", my_set | {3, 4})  # union


    print("\n-- Dictionary Expressions --")
    my_dict = {"a": 1, "b": 2}
    print("my_dict ->", my_dict)
    print("my_dict['a'] ->", my_dict["a"])
    print("list(my_dict.keys()) ->", list(my_dict.keys()))
    
if __name__ == "__main__":
    run()