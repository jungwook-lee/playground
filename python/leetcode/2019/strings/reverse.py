def reverse(x):
    out = 0
    mod_val = 10 if x >= 0 else -10
    while x != 0:
        temp = x % mod_val
        x = int(x / 10)
        if out * 10 + temp > (2**31)-1:
            return 0
        if out * 10 - temp < -(2**31):
            return 0

        out = out * 10 + temp
    return out

print(reverse((2**31)-1))
print(reverse(-(2**31)))
print(reverse(123))
print(reverse(-123))
print(reverse(120))
print(reverse(0))
print(reverse(1))
print(reverse(-1))