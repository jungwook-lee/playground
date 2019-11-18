# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        def helper(out, root, level=0):
            if root is None:
                return out
            if len(out) - 1 < level:
                out.append([])
            out = helper(out, root.left, level + 1)
            out = helper(out, root.right, level + 1)
            out[level].append(root.val)
            return out

        return helper([[]], root)