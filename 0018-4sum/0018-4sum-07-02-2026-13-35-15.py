class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans, li = [], []
        # fix 2 nums, subtract from target then 2sum to find other two
        for i in range(len(nums)):
            # skip if repeat
            if i > 0 and nums[i] == nums[i-1]:
                continue
            n1 = nums[i]
            for j in range(i+1, len(nums)): 
                # skip curr(j) if same as prev
                if j > i + 1 and nums[j - 1] == nums[j]:
                    continue              
                n2 = nums[j]
                rem = target - (n1 + n2)
                # two pointer starts here
                l, r = j + 1, len(nums) - 1
                while l < r:
                    s = nums[l] + nums[r]
                    if s > rem: 
                        r -= 1
                    elif s < rem:
                        l += 1
                    else:
                        ans.append([n1, n2, nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while (l < r and nums[l] == nums[l - 1]):
                            l += 1

        return ans
        

    
        