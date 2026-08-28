def topKFrequent(self, nums: list[int], k: int) -> list[int]:
    hashNums = {}
    n = len(nums)
    freq = [[] for i in range(n+1)]

    for n in nums:
        hashNums[n] = 1 + hashNums.get(n,0)
    for n,c in hashNums.items():
        freq[c].append(n)

    res = []
    for i in range(len(freq) -1, 0, -1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res
