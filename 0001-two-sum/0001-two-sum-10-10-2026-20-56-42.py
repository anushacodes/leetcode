class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        prev = {}

        for i, num in enumerate(nums):
            comp = target - num
            if comp in prev:
                return ([i, prev[comp]])
            else:
                prev[num] = i
                # print (prev)
            


        