from tree import TreeNode, Tree

def isMatch(s,t):
    if (s is None and t is not None) or (s is not None and t is None):
        return False
    elif s is None and t is None:
        return True
    return s.val == t.val and isMatch(s.left, t.left) \
                          and isMatch(s.right, t.right)

def isSubtree(s, t):
    if isMatch(s, t):
        return True
    if not s:
        return False
    return isSubtree(s.left, t) or isSubtree(s.right, t)

if __name__ == '__main__':
    s_in=[4, 1, 2, 4, None, None, None, 1]
    s = Tree(s_in)

    t_in=[4, 1]
    t = Tree(t_in)

    print(isSubtree(s.head, t.head))
    s.print_tree()
