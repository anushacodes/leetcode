class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        dupemap = set()

        for num in nums:
            if num in dupemap:
                return num
            else:
                dupemap.add(num)


        