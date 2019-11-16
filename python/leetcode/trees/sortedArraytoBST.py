# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # Iterative Solution

    # def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
    #     if not nums:
    #         return None
    #
    #     mid = (len(nums) - 1) // 2
    #     root = TreeNode(nums[mid])
    #
    #     cur_n = root
    #     for i in range(mid - 1, -1, -1):
    #         temp = TreeNode(nums[i])
    #         cur_n.left = temp
    #         cur_n = temp
    #
    #     cur_n = root
    #     for i in range(mid + 1, len(nums)):
    #         temp = TreeNode(nums[i])
    #         cur_n.right = temp
    #         cur_n = temp
    #
    #     return root

    # Recursive Solution
    # Space O(n) to save all node in the stack
    # Runtime O(n) to traverse through every element in the list

    class Solution:
        def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
            if not nums:
                return None

            def convert(low, high, nums):
                if high < low or low > high:
                    return None
                mid = (high - low) // 2
                mid += low
                node = TreeNode(nums[mid])
                node.left = convert(low, mid - 1, nums)
                node.right = convert(mid + 1, high, nums)
                return node

            return convert(0, len(nums) - 1, nums)