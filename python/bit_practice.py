import sys

# Test bit manipulation in python

# Python Natively only has logical shifts
def repeatedArithmeticShift(var, count=40):
    for i in range(count):
        var >>= 1
    return var

if __name__ == '__main__':
    test_var = -13
    print(repeatedArithmeticShift(test_var))