def lengthOfLongestSubstring(s: str) -> int:
    # first solution: O(n^2)
    if len(s)==1:
        return 1
    l,r = 0, 0
    res = 0
    curr = 0
    while l<=r and r<=len(s)-1:
        if not s[r]:
            return res
        if (s[r] in s[l:r]):
            res = max(curr, res)
            curr = 0
            l+=1
            r = l
            continue
        r+=1
        curr +=1
            

    
    return max(res,curr)

