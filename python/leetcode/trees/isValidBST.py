class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def helper(root, l_limit=float("-inf"), h_limit=float("inf")):
            if not root:
                return True

            if root.val > l_limit and root.val < h_limit:
                if not helper(root.right, root.val, h_limit):
                    return False
                if not helper(root.left, l_limit, root.val):
                    return False
                return True
            else:
                return False

        return helper(root)