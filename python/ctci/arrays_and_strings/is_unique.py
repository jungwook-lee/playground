def is_unique(in_str):
    ht = dict()
    for char in in_str:
        # Check if char is in the ht
        if not ord(char) in ht:
            ht[ord(char)] = 1
        else:
            return False
    return True

def is_unique_bit(in_str):
    bv = int(0)
    for char in in_str:
        char_bit = 1 << (ord(char) - ord('a'))
        if bv & char_bit:
            return False
        bv |= char_bit
    return True

if __name__ == '__main__':
    test = 'abcde'
    print(is_unique(test))
    test = 'abcdea'
    print(is_unique(test))

    test = 'abcde'
    print(is_unique_bit(test))
    test = 'abcdea'
    print(is_unique_bit(test))
