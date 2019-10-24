# Implement fibonacci number with memoization -> O(n)
def fib(n):
    cache = {}
    def recur_fib(n):
        if n in cache:
            return cache[n]
        if n < 2:
            result = n
        else:
            result = recur_fib(n-1) + recur_fib(n-2)

        cache[n] = result
        return result

    return recur_fib(n)

if __name__ == '__main__':
    n = 30
    print(fib(n))