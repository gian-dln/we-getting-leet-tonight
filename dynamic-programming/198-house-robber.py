def rob(nums: list[int]) -> int:
    rob1, rob2 = 0, 0
    for n in nums:
        # nums = [5, 1, 2, 6, 20]
        newRob = max(rob1 + n, rob2) #
        rob1 = rob2
        rob2 = newRob

    return rob2
