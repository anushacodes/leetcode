class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        max_value = max(nums) - min(nums)

        return k * max_value

        
