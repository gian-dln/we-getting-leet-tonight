def subsets(nums: list[int]) -> list[list[int]]:
    # res = []
    # subset = []

    # def dfs(i):
    #     if i >= len(nums):
    #         res.append(subset.copy())
    #         return
        
    #     subset.append(nums[i])
    #     dfs(i+1)

    #     subset.pop()
    #     dfs(i+1)
        
    
    # dfs(0)

    res = [[]]
    subset = []
    for n in nums:
        res += [subset + [n] for subset in res]

    '''
    [1,2,3]
    res = [], + [] + 1, 
    res = [],[1]
    res = [], [1]
    res = [], [1], [2], [1,2]
    res = [], [1], [2], [1,2], [3], [1,3], [2,3], [1,2,3]
    '''
    return res