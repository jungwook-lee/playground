class Solution:
    def isOverlap(self, a, b):
        left, right = 0, 1
        if a[left] <= b[left] <= a[right]:
            return True
        if a[left] <= b[right] <=a[right]:
            return True
        if a[left] >= b[left] and a[right] <= b[right]:
            return True
        return False

    def insert(self, intervals, newInterval):
        j = 0
        _min, _max = 0, 1
        while j < len(intervals):
            cur_interval = intervals[j]
            if isOverlap(cur_interval, newInterval):
                cur_interval[_min] = min(cur_interval[_min], newInterval[_min])
                cur_interval[_max] = max(cur_interval[_max], newInterval[_max])
            j += 1
        return intervals

if __name__ == '__main__':
    sol = Solution()
    test = [[1,3], [6,9]]
    newInt = [4,8]
    exp = [[1,5],[6,9]]
    assert (sol.insert(test, newInt) == exp)

    test = [[1,2], [3,5], [6,7], [8,10], [12,16]]
    newInt = [4,8]
    exp = [[1,2],[3,10],[12,16]]
    assert (sol.insert(test, newInt) == exp)

