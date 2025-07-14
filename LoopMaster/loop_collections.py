def run():
    print("\n-- Looping Over Collections --")

    my_list = [10, 20, 30]
    print("List:")
    for item in my_list:
        print(item)

    my_dict = {"a": 1, "b": 2}
    print("\nDictionary:")
    for key, value in my_dict.items():
        print(f"{key} => {value}")

    print("\nUsing enumerate():")
    for index, value in enumerate(["x", "y", "z"]):
        print(index, value)
