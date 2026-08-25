def maxArea(height: list[int]) -> int:
    n = len(height)
    lo,hi = 0, n-1
    length = hi-lo
    maxArea = 0

    while lo < hi:
        area = min(height[lo], height[hi]) * length
        if min(height[lo], height[hi]) == height[lo]:
            lo += 1
            length -= 1
        elif min(height[lo], height[hi]) == height[hi]:
            hi -= 1
            length -= 1
        maxArea = max(maxArea, area)

    return maxArea


height = [1,8,6,2,5,4,8,3,7]

print(maxArea(height))