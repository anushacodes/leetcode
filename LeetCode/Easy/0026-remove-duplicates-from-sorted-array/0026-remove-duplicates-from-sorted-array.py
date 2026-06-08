class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # a set to check each num, c = 0
        # if in set then set to inf 
        # if not in set then add to set and increase count
        # sort and return arr

        h = set()
        c = 0

        for i in range (len(nums)):
            if nums[i] in h:
                nums[i] = inf
            elif nums[i] not in h:
                h.add(nums[i])
                c += 1

        nums.sort()
        return c


        
