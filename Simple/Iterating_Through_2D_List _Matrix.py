print("\nExample 3: Iterating Through a 2D List (Matrix)")
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix : 
    for el in row :
        print(el , end=" ")
    print()