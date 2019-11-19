# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """

        def helper(start, end, latest):
            if start == end:
                return start
            elif start == latest:
                if not isBadVersion(latest):
                    return 0
                return latest

            mid = (end + start) // 2
            if isBadVersion(mid):
                return helper(start, mid, latest)
            else:
                return helper(mid + 1, end, latest)
            return val

        return helper(1, n, n)