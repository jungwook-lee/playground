# Pretty slow approach
def non_overlapping_intervals(intervals):
    start, end = 0, 1
    # how to solve overlapping interval problems:
    # 1. sort the intervals in increasing order of their start position
    intervals.sort()
    # 2. scan the sorted interval and maintain an active set
    count, minEnd = 0, None
    
    for interval in intervals:
        if not minEnd:
            minEnd = interval[end]
        if interval[start] >= minEnd:
            # non-overlap, start new active set
            minEnd = interval[end]
        else:
            # overlap, record param
            count += 1
            minEnd = min(minEnd, interval[end])
    return count - 1

# Optimized code
def eraseOverlapIntervals(intervals):
    end = float('-inf')
    _start, _end = 0, 1
    erased = 0
    intervals.sort(key=lambda i: i[_start])
    for i in intervals:
        if i[_start] >= end:
            end = i[_end]
        else:
            erased += 1
    return erased


if __name__ == '__main__':
    test = [[1,2],[2,3],[3,4],[1,3]]
    print(non_overlapping_intervals(test))

    test = [[1,2],[1,2],[1,2]]
    print(non_overlapping_intervals(test))

    test = [[1,2],[2,3]]
    print(non_overlapping_intervals(test))
    print(eraseOverlapIntervals(test))

