def print_reverse(string):
    if len(string) == 0:
        return

    print_reverse(string[1:])
    print(string[0])


if __name__ == '__main__':
    input_1 = ["h","e","l","l","o"]
    print_reverse(input_1)
    input_2 = ["H","a","n","n","a","h"]
    print_reverse(input_2)