# Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.
# Note that the row index starts from 0.

def getRow(numRows):
    out_arr = [1] * (numRows + 1)
    # Build the list
    for i in range(0, numRows - 1):
        for j in range(i, -1, -1):
            out_arr[j+1] += out_arr[j]
    return out_arr


if __name__ == '__main__':
    input = 4
    print(getRow(input))

