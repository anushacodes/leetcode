class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        max = 0
        # next = nums[i+1]
        for i in nums:
            if i == 1:
                count += 1
                if max < count:
                    max = count
            elif i != 1:
                count = 0
            
        return max
            

        




        