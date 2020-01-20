def climbStairs(n):
    cache = {}
    def recur_climb(n):
        if n in cache:
            return cache[n]

        # base case
        if n == -1:
            return 0
        if n == 0:
            return 1

        result = recur_climb(n - 1) + recur_climb(n - 2)
        cache[n] = result
        return result

    return recur_climb(n)


if __name__ == '__main__':
    input = 100
    print(climbStairs(input))