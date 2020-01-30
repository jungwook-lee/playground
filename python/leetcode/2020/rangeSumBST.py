class Solution(object):
    def rangeSumBST(self, root, L, R):
        if not root:
            return 0
        val = root.val
        if val < L or val > R:
            val = 0
        return val + self.rangeSumBST(root.left, L, R) \
                   + self.rangeSumBST(root.right, L, R)
