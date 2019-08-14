def urlify(str, len):
    # count how many spaces
    space_cnt = 0
    for i in range(len):
        if str[i] == " ":
            space_cnt += 1
    # Figure out the new output string
    new_size = len + (2 * space_cnt)
    j = new_size - 1

    # In python str are immutable
    # make a list and then join them at the end
    out_str = [' '] * new_size
    for i in range(len - 1, -1, -1):
        if str[i] != " ":
            out_str[j] = str[i]
            j -= 1
        else: # str[i] is ' '
            out_str[j] = '0'
            out_str[j-1] = '2'
            out_str[j-2] = '%'
            j -= 3
    return ''.join(out_str)

if __name__ == '__main__':
    input_str = "Mr John Smith    "
    true_len = 13
    print(urlify(input_str, true_len))