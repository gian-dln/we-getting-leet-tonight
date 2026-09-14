def maxSubArray(self, nums: list[int]) -> int:
    maxSum = nums[0]
    currentSum = 0

    for n in nums:
        if currentSum < 0:
            currentSum = 0
        currentSum += n
        maxSum = max(maxSum, currentSum)

    return maxSum