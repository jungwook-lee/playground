from tree import TreeNode, Tree

""" Brute Force
def lowestCommonAncestor(root, p, q):
    if p <= root.val <= q:
        if isAncestor(root, p) and isAncestor(root, q):
            return root
        else:
            return None
    else:
        if root.val > q:
            lca = lowestCommonAncestor(root.left, p, q)
        elif root.val < p:
            lca = lowestCommonAncestor(root.right, p, q)
        return lca
    

def isAncestor(root, val):
    if root is None:
        return False
    if root.val == val:
        return True
    if val < root.val:
        return isAncestor(root.left, val)
    elif root.val < val:
        return isAncestor(root.right, val)
"""

""" Runtime of O(n) with space (due to stack) O(n)
def lowestCommonAncestor(root, p, q):
    if not root:
        return None
    if min(p, q) > root.val:
        return lowestCommonAncestor(root.right, p, q)
    elif max(p, q) < root.val:
        return lowestCommonAncestor(root.left, p, q)
    else:
        return root
"""

# Best Implementation O(N) and O(1)
def lowestCommonAncestor(root, p, q):
    while root:
        if min(p, q) > root.val:
            root = root.right
        elif max(p, q) < root.val:
            root = root.left
        else:
            return root

if __name__ == '__main__':
    tree = Tree([6,2,8,0,4,7,9,None,None,3,5])
    print(lowestCommonAncestor(tree.head, p=2, q=8))
    print(lowestCommonAncestor(tree.head, p=2, q=4))
    print(lowestCommonAncestor(tree.head, p=7, q=9))
    print(lowestCommonAncestor(tree.head, p=0, q=5))
    print(lowestCommonAncestor(tree.head, p=3, q=5))
