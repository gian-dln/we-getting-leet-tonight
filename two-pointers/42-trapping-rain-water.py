def trap(self, height: list[int]) -> int:
    n = len(height)
    l,r = 0, n-1
    maxL,maxR = height[l], height[r]
    res = 0

    while l < r:
        if min(maxL, maxR) == maxL:
            l += 1
            maxL = max(maxL, height[l])
            res += maxL - height[l]
        else:
            r -= 1
            maxR = max(maxR, height[r])
            res += maxR - height[r]


    return res

