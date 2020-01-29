from tree import TreeNode, Tree

# First attempt
#def diameterOfBinaryTree(root):
#    if root is None:
#        return 0
#    if root.left is None and root.right is None:
#        return 1
#    if not root.left is None and root.right is None:
#        return 1
#    if root.left is None and not root.right is None:
#        return 1
#    return diameterOfBinaryTree(root.left) + diameterOfBinaryTree(root.right)

class Solution(object):
    def __init__(self):
        pass

    def diameterOfBinaryTree(self, root):
        self.ans = 0
        def depth(root):
            if not root:
                return 0
            L = depth(root.left)
            R = depth(root.right)
            self.ans = max(self.ans, L+R)
            return max(L, R) + 1
        depth(root)
        return self.ans

if __name__ == '__main__':
    tree = Tree([1,2,3,4,5])
    solution = Solution()
    print(solution.diameterOfBinaryTree(tree.head))
    
    tree = Tree([1])
    solution = Solution()
    print(solution.diameterOfBinaryTree(tree.head))
 
