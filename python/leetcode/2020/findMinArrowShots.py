def findMinArrowShots(points):   
    if points is None or len(points) == 0:
        return 0
    
    _left, _right = 0, 1
    points.sort(key=lambda i:i[_right])
    minEnd = float('-inf')
    shots = 0
    for balloon in points:
        if balloon[_left] > minEnd:
            # Not inside
            minEnd = balloon[_right]
            shots += 1
        else:
            # inside minEnd
            minEnd = min(minEnd, balloon[_right])
    return shots

if __name__ == '__main__':
    test=[[10,16], [2,8], [1,6], [7,12]]
    print(findMinArrowShots(test))
