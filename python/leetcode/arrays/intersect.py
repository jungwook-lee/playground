import collections

def intersect_v1(nums1, nums2):
    # Assume that int's are 0-9
    mem = dict(zip(range(10), [0] * 10))
    for num in nums1:
        mem[num] += 1
    out = []
    for num in nums2:
        if mem[num] > 0:
            mem[num] -= 1
            out.append(num)
    return out

def intersect_v2(nums1, nums2):
    # O(nlogn) Worst time
    nums1 = sorted(nums1)
    nums2 = sorted(nums2)

    i, j, out = 0, 0, []
    while i < len(nums1):
        if nums1[i] == nums2[j]:
            out.append(nums1[i])
            i += 1
            j += 1
        elif nums1[i] > nums2[j]:
            j += 1
        else:
            i += 1
    return out

def intersect_v3(nums1, nums2):
    # Assume that int's 2^32
    # Space usage here would be O(n)
    mem = collections.defaultdict(int)
    for num in nums1:
        mem[num] += 1
    out = []
    for num in nums2:
        if mem[num] > 0:
            mem[num] -= 1
            out.append(num)
    return out

test_arr1 = [4,9,5]
test_arr2 = [9,4,9,8,4]
print(intersect_v1(test_arr1, test_arr2))

test_arr1 = [1,2,2,1]
test_arr2 = [2,2]
print(intersect_v1(test_arr1, test_arr2))

test_arr1 = [1,2,2,1]
test_arr2 = [2,2]
print(intersect_v2(test_arr1, test_arr2))

test_arr1 = [4,9,5]
test_arr2 = [9,4,9,8,4]
print(intersect_v2(test_arr1, test_arr2))

test_arr1 = [4,9,5, 4241,59123]
test_arr2 = [9,4,9,8,4, 1241, 59123]
print(intersect_v3(test_arr1, test_arr2))

# print(intersect_v1(test_arr1, test_arr2))