class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        h = set()
        for num in nums:
            h.add(num)
        return len(h) != len(nums)
        