# My First Attempt Solution

# def maxSubArray(nums):
#     if not nums:
#         return 0
#
#     arr = [nums[0]] * len(nums)
#     for i in range(1, len(nums)):
#         arr [i] = arr[i-1] + nums[i]
#     max_i = 0
#     for i in range(1, len(arr)):
#         if arr[max_i] < arr[i]:
#             max_i = i
#     min_i = 0
#     for i in range(1, max_i + 1):
#         if arr[min_i] > arr[i]:
#             min_i = i
#     return arr[max_i] - arr[min_i]


def maxSubArray(nums):
    def max(new_start, cum_sum):
        if cum_sum < new_start:
            return new_start
        else:
            return cum_sum
    cum_sum = nums[0]
    max_sum = nums[0]
    for i in range(1, len(nums)):
        cum_sum += nums[i]
        cur_max = max(nums[i], cum_sum)
        cum_sum = cur_max

        if cur_max > max_sum:
            max_sum = cur_max

    return max_sum


if __name__ == '__main__':
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(maxSubArray(nums))

    nums = [-1, -2, -1, -2, 6, -3]
    print(maxSubArray(nums))

    nums = [1]
    print(maxSubArray(nums))

    nums = [1,2]
    print(maxSubArray(nums))

    nums = [1,2,3,3]
    print(maxSubArray(nums))

