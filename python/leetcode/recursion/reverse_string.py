"""
Write a function that reverses a string. The input string is given as an array of characters char[].
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
You may assume all the characters consist of printable ascii characters.
"""

# Iterative Version
def reserse_string(str):
    if len(str) < 1:
        return

    for i in range(int(len(str) // 2)):
        str[i], str[len(str) - (i + 1)] =  str[len(str) - (i + 1)], str[i]

if __name__ == '__main__':
    input_1 = ["h","e","l","l","o"]
    reserse_string(input_1)
    print(input_1)
    input_2 = ["H","a","n","n","a","h"]
    reserse_string(input_2)
    print(input_2)