def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    diff = dict()
    for i in range(len(nums)):
        diff[target - nums[i]] = i
    for j in range(len(nums)):
        if nums[j] in diff and diff[nums[j]] != j:
            return [j, diff[nums[j]]]

def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    diff = dict()
    for i in range(len(nums)):
        complement = target - nums[i]
        if nums[i] in diff:
            return [i, diff[nums[i]]]
        diff[complement] = i
