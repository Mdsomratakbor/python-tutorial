def run():
    print("\n-- 2D List Comprehension --")
    rows, cols = 3, 3
    matrix = [[row * col + 1 for col in range(cols) ] for row in range(rows)]
    print("3x3 Matrix:")
    for row in matrix:
        print(row)
