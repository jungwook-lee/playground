class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        table = dict()
        for elem in nums:
            if not elem in table:
                table[elem] = 1
            else:
                table[elem] += 1
        for _, val in table.items():
            if val > 1:
                return True
        return False


