def two_sum(nums, t):
    ht = dict()
    for i in range(len(nums)):
        comp = t - nums[i]
        if comp in ht and ht[comp] != i:
            return [i, ht[comp]]
        ht[nums[i]] = i

if __name__ == '__main__':
    test = [2, 7, 11, 15]
    print(two_sum(test, 9))
    test = [-17, -2, 0, 5, 10]
    print(two_sum(test, 7))
    print(two_sum(test, -7))
    test = [0, 1]
    print(two_sum(test, 1))
    test = [3, 2, 4]
    print(two_sum(test, 6))
    test = [3, 3]
    print(two_sum(test, 6))
