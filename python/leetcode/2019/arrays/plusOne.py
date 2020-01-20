def plusOne(digits):
    if digits[-1] < 9:
        digits[-1] += 1
        return digits

    if digits[-1] == 9:
        if len(digits) == 1:
            return [1, 0]
        else:
            return plusOne(digits[:len(digits)-1]) + [0]

print (plusOne([1,2,3,4]))
print (plusOne([1,2,9]))
print (plusOne([9]))
print (plusOne([1,9,9]))
print (plusOne([9,9,9,9,9,9]))