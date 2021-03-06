# O(n * k) runtime, O(1) space
# def rotate_array(nums, k):
#     for _ in range(k):
#         temp = nums[-1]
#         # simplest method to store temp and move up
#         for i in range(len(nums)):
#             nums[i], temp = temp, nums[i]
#     print(nums)

# O(n), but O(n) space
# def rotate_array(nums, k):
#     out = [0] * len(nums)
#     for i in range(len(nums)):
#         new_i = (i + k) % len(nums)
#         out[new_i] = nums[i]
#     print(out)

# def reverse_arr(nums):
#     for i in range(len(nums)//2):
#         end_i = len(nums) - i - 1
#         nums[i], nums[end_i] = nums[end_i], nums[i]
#     return nums
#
# # Reversing option O(n), O(1)
# def rotate_array(nums, k):
#     nums = reverse_arr(nums)
#     nums[0:k] = reverse_arr(nums[0:k])
#     nums[k:] = reverse_arr(nums[k:])
#     print(nums)

# Using cycle dependency method, O(n) time, O(1) space
def rotate_array(nums, k):
    n = len(nums)
    n_swaps = 0
    i, start = 0, 0
    while(n_swaps < n):
        i = start
        temp = nums[i]
        while True:
            next_i = (i + k) % len(nums)
            nums[next_i], temp = temp, nums[next_i]
            n_swaps += 1
            # Handle cycle dependency
            if next_i == start:
                break
            else:
                i = next_i
        start += 1
    print(nums)

if __name__ == '__main__':
    test_nums = [1,2,3,4,5,6,7]
    k = 3
    rotate_array(test_nums, k)

    test_nums = [1,2,3,4]
    k = 2
    rotate_array(test_nums, k)

    test_nums = [-1, -100, 3, 99]
    k = 2
    rotate_array(test_nums, k)