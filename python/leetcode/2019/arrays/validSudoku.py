def validSudoku(board):
    """
    :param board: array of strings
    :return:
    """
    for i in range(len(board)):
        mem = dict(zip(range(1, 10), [0] * 9))
        for j in range(len(board)):
            val = board[i][j]
            if val == '.':
                continue
            else:
                val = int(val)
            mem[val] += 1
            if mem[val] > 1:
                return False

    for i in range(len(board)):
        mem = dict(zip(range(1, 10), [0] * 9))
        for j in range(len(board)):
            val = board[j][i]
            if val == '.':
                continue
            else:
                val = int(val)
            mem[val] += 1
            if mem[val] > 1:
                return False

    for x in range(3):
        for y in range(3):
            mem = dict(zip(range(1, 10), [0] * 9))
            for i in range(0 + x * 3 , 3 + x * 3):
                for j in range(0 + y * 3, 3 + y * 3):
                    val = board[i][j]
                    if val == '.':
                        continue
                    else:
                        val = int(val)
                    mem[val] += 1
                    if mem[val] > 1:
                        return False
    return True

test_board = [
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
print(validSudoku(test_board))

test_board = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
print(validSudoku(test_board))