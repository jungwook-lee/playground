from tree import TreeNode, Tree

""" Time complexity is O(m) where m is
    the number of nodes, since at the worst
    case, we end up traversing through all
    the nodes. 

    The Space complexity is O(m) where the
    recursion stack will have maximum of m when
    the execusion tree is skewed to one side. 
    Average case would be O(log m)
"""

def mergeTrees(t1, t2):
    if t1 is None and t2 is None:
        return None
    new_n = TreeNode(0)
    if t1 is None and not t2 is None:
        new_n.val = t2.val
    elif not t1 is None and t2 is None:
        new_n.val = t1.val
    else:
        new_n.val = t1.val + t2.val

    # merge left
    new_n.left = mergeTrees(
        t1.left if t1 else None,
        t2.left if t2 else None
    )
    # merge right
    new_n.right = mergeTrees(
        t1.right if t1 else None,
        t2.right if t2 else None
    )
    return new_n

# Don't make a new node
#def mergeTrees(t1, t2):
#    if t1 is None:
#        return t2
#    if t2 is None:
#        return t1
#    t1.val += t2.val
#    t1.left = mergeTrees(t1.left, t2.left)
#    t1.right = mergeTrees(t2.right, t2.right)
#    return t1

if __name__ == '__main__':
    tree_1 = Tree([1,3,2,5])
    tree_2 = Tree([2,1,3,None,4,None,7])
    merged = mergeTrees(tree_1.head, tree_2.head)
    merged_tree = Tree([])
    merged_tree.head = merged
    merged_tree.print_tree()
    
