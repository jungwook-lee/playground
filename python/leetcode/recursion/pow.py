# # Not using tail recursion
# def myPow(x, n):
#     """
#     :type x: float
#     :type n: int
#     :rtype: float
#     """
#     if n == 0:
#         return 1
#
#     if n > 0:
#         return x * myPow(x, n-1)
#     else:
#         return (1 / x) * myPow(x, n+1)

# Use tail recursion, Space complexity of O(log n)
def myPow(x, n):
    if not n:
        return 1
    if n < 0:
        return 1 / myPow(x, -n)
    if n % 2:
        # odd case
        return x * myPow(x, n-1)
    return myPow(x*x, n/2)

if __name__ == '__main__':
    print(myPow(2.00000, 10))
    print(myPow(2.10000, 3))
    print(myPow(2.00000, -2))

    print(myPow(1.00001, 123456))