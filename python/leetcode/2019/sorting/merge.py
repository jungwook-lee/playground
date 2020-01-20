def merge(nums1, m, nums2, n):
    if not nums1 and not nums2:
        return []
    if not nums2:
        return nums1

    i, j = 0, 0
    while j < n:
        if i >= m:
            nums1[i] = nums2[j]
            i += 1
            m += 1
            j += 1
            continue

        while nums1[i] <= nums2[j] and i < m:
            i += 1

        if i < m:
            for x in range(m, i, -1):
                nums1[x] = nums1[x - 1]

        nums1[i] = nums2[j]
        i += 1
        j += 1
        m += 1
    return nums1

print(merge([1,2,3,0,0,0], 3, [2,5,6], 3))
print(merge([1,3,5,0,0,0], 3, [2,4,6], 3))
print(merge([1,5,0,0,0], 2, [2,4,6], 3))
print(merge([2,3,5,0], 3, [1], 1))
print(merge([2,0], 1, [1], 1))
print(merge([0], 0, [1], 1))