class Solution:
    def smallestIndex(self, nums: list[int]) -> int:
        # 10%10 = 0
        # 1%10 = 1
        for i, n in enumerate(nums):
            if self.sumDigits(n) == i:
                return i
        
        return -1

    def sumDigits(self, n: int) -> int:
        if (n<10):
            return n
        
        return (n % 10) + self.sumDigits(n // 10)
    
                