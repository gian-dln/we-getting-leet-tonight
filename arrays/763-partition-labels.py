def partitionLabels(s: str) -> list[int]:
    seen = {}
    res = []
    l = r = 0

    for i, c in enumerate(s):
        seen[c] = i

    for i, c in enumerate(s):
        r = max(seen[c], r)
        if i == r:
            res.append(r-l+1)
            l = i+1
    

    return res

