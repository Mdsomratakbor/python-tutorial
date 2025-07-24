def run():
    print("\n-- Matrix Operations --")
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    
    # sum of all elements
    
    total = sum((sum(row) for row in matrix))    
    print(f"Sum: {total}")
    
    
    
    # Transpose
    #transpose = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    
    transpose = []
    
    rows = len(matrix)
    cols = len(matrix[0])
    
    for i in range(cols):
        new_row =[]  
        for j in range(rows):
            new_row.append(matrix[j][i])
        
        transpose.append(new_row)
    print("Transpose:")
    for row in transpose:
        print(row)
