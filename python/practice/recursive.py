def factorial(num):

    # base case
    if num == 0:
        return 1
    else:
        # recursive case
        return num * factorial(num - 1)


def binary_search(data, target, low, high):
    if low > high:
        return False

    mid = int((high + low) / 2)
    # or

    # base case
    if data[mid] == target:
        return mid

    # recursive cases
    if data[mid] > target:
        return binary_search(data, target, low, mid - 1)
    if data[mid] < target:
        return binary_search(data, target, mid + 1, high)


def fib(num):
    # returns F(n), F(n-1)
    # base case
    if num <= 1:
        return num, 0
    else:
        # a = F(n-1) + F(n), b = F(n)
        a, b = fib(num - 1)
        return a+b, a


if __name__ == '__main__':
    # Test the factorial function
    n = 6
    print(factorial(n))

    # Test the binary search
    n = [2, 4, 5, 7, 8, 9, 12, 14, 17, 19]
    print(n)

    print(binary_search(n, 14, 0, len(n) - 1))

    n = 6
    print(fib(n))
