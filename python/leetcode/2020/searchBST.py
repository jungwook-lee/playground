from tree import TreeNode, Tree

def searchBST(root, val):
    if not root:
        return None
    elif root.val == val:
        return root
    elif root.val > val:
        return searchBST(root.left, val)
    elif root.val < val:
        return searchBST(root.right, val)

if __name__ == '__main__':
    tree = Tree([4,2,7,1,3])
    #tree.print_tree()
    print(searchBST(tree.head, 2))
