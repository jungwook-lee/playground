def kthGrammar(N, K):
    if N == 1 and K == 1:
        return 0

    out = kthGrammar(N - 1, int((K + 1) // 2))
    # invert if 1
    return ((K - 1) % 2) ^ out

if __name__ == '__main__':

    print(kthGrammar(4, 5))
    print(kthGrammar(4, 6))
    print(kthGrammar(4, 7))
    print(kthGrammar(4, 8))

    print([kthGrammar(5, i) for i in range(1, 17)])
