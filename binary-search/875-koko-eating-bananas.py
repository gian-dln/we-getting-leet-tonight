def minEatingSpeed(self, piles: list[int], h: int) -> int:
    # i =  bananas per hour, n = bananas in pile
    l,r = 1, max(piles)
    res = max(piles)
    while l <= r:
        mid = (l+r)//2
        total = 0
        for p in piles:
            total += math.ceil(float(p)/mid)
        if total <= h:
            res = mid
            r = mid-1
        else:   
            l = mid+1


    
    return res


