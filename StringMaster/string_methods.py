def run():
    print("\n-- String Methods --")
    raw = "   spaced   "
    print("Before strip:", repr(raw))
    print("After strip :", repr(raw.strip()))

    word = "python"

    print("Uppercase:",word.upper())
    print("lowercase:",word.lower())
    print("Capitalize:", word.capitalize())
    print("Title:", word.title())
    print("Replace 'p' with '*':", word.replace('p', '*'))
    print("Startswith 'py':", word.startswith('py'))
    print("Endswith 'on':", word.endswith('on'))
    print("Find 'on':", word.find('on'))