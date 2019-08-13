# Python Natively only has logical shifts
def repeatedArithmeticShift(var, count=40):
    for i in range(count):
        var >>= 1
    return var

def getBit(num, i):
    return (num & (1 << i - 1) != 0)

def setBit(num, i):
    return num | (1 << i - 1)

def clearBit(num, i):
    return num & ~(1 << i - 1)

def updateBit(num, i, val):
    # Clear then set
    mask = ~(1 << i - 1)
    return (num & mask) | (val << i - 1)


if __name__ == '__main__':
    test_var = -13
    print(repeatedArithmeticShift(test_var))

    test_var = 18
    print(bin(test_var))
    print(getBit(test_var, 2))
    print(getBit(test_var, 3))

    print(bin(setBit(test_var, 3)))
    print(bin(clearBit(test_var, 3)))

    print(bin(updateBit(test_var, 5, 0)))
    print(bin(updateBit(test_var, 5, 1)))