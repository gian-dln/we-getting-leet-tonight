def maxArea(height: list[int]) -> int:
    n = len(height)
    lo,hi = 0, n-1
    length = hi-lo
    maxArea = 0

    while lo < hi:
        loHeight = height[lo]
        hiHeight = height[hi]
        area = min(loHeight, hiHeight) * length
        if loHeight < hiHeight:
            lo += 1
            length -= 1
        else:
            hi -= 1
            length -= 1
        maxArea = max(maxArea, area)

    return maxArea


height = [1,8,6,2,5,4,8,3,7]

print(maxArea(height))
