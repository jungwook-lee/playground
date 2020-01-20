# Simple positive sum only
def sum_of_two_integers(a, b):
    # First get the carry
    while b != 0:
        car = a and b
        a = a ^ b
        b = car << 1
    return a

# Negative solution to implement
# https://leetcode.com/problems/sum-of-two-integers/discuss/84282/Python-solution-with-no-%22%2B-*%22-completely-bit-manipulation-guaranteed

if __name__ == '__main__':
    print(sum_of_two_integers(-3, 1))
