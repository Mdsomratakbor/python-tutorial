def run():
    print("\n-- Loop Over 2D List --")
    matrix = [[1, 2], [3, 4], [5, 6]]
    
    print("Row-Wise: ")
    
    for row in matrix:
        print(row)
        
    print("Element-Wise: ")
    
    for row in matrix:
        for col in row:
            print(col, end=" ")
        print()