def productExceptSelf(nums):
    L = [1] * len(nums)
    R = [1] * len(nums)
    output = []

    for i in range(len(nums) - 1):
        L[i + 1] = L[i] * nums[i]

    for i in range(len(nums) - 1, 0, -1):
        R[i - 1] = R[i] * nums[i]

    for i in range(len(nums)):
        output.append(L[i] * R[i])

    return output


if __name__ == '__main__':
    test_list = [1, 2, 3, 4]
    print(productExceptSelf(test_list))