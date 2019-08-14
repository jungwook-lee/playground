import sys

def bit_insertion(N, M, j, i):
    mask = (1 << (j + 1)) - (1 << i)
    return (N & ~mask) | (M << i)

if __name__ == '__main__':
    n = 0b11111111
    m = 0b00100
    i, j = 1, 5

    out = bit_insertion(n, m, j, i)
    print(bin(out))