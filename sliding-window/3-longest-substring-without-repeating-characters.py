def lengthOfLongestSubstring(s: str) -> int:
    # optimized O(n)
    l = 0
    res = 0
    chars = set()
    
    for r in range(len(s)):
        while s[r] in chars:
            chars.remove(s[l])
            l+=1
        
        chars.add(s[r])
        res = max(res, r-l+1) #r-l+1 = len(s[l:r])
    
    return res