# Runtime O(n), Space O(n)

# class Solution:
#     def hasCycle(self, head: ListNode) -> bool:
#         mem = dict()
#         cur = head
#         while cur != None:
#             if id(cur) in mem:
#                 return True
#             else:
#                 mem[id(cur)] = 1
#             cur = cur.next
#         return False

# Best Solution Runtime O(n + k) where k is cyclic length, O(1) Space
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False

        p_s, p_f = head, head
        while p_f != None:
            p_s = p_s.next
            if p_f.next == None:
                return False
            else:
                p_f = p_f.next.next
            if p_s == p_f:
                return True
        return False