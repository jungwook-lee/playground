def generate(numRows):
    pascal_tri = []
    # Build the list
    for i in range(1, numRows + 1):
        pascal_tri.append([pascal(pascal_tri, i, j) for j in range(1, i + 1)])
        print(i, pascal_tri)
    return pascal_tri


def pascal(table, i, j):
    # Base Case
    if j == 1 or j == i:
        return 1
    # Recurrence relation
    return table[i - 2][j - 1] + table[i - 2][j - 2]


if __name__ == '__main__':
    print(generate(25))
