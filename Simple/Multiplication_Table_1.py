print("\nExample 2: Creating a Multiplication Table")
print("Multiplication Table (1-5)")
for i in range(1, 6):  # Rows for numbers 1 to 5
    for j in range(1, 6):  # Columns for numbers 1 to 5
        product = i * j
        print(f"{j} * {i} = {product}\t", end="") # \t for tab spacing, end="" to stay on same line
    print() # Newline after each row