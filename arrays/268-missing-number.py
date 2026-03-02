def missingNumber(nums: list[int]) -> int:
        return sum(range(len(nums)+1)) - sum(nums)
