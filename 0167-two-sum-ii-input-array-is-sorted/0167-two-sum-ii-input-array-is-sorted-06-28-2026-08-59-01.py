class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1

        while l < r:
            low = nums[l]
            high = nums[r]

            sum = low + high

            if sum < target:
                l += 1
            elif sum > target:
                r -= 1
            elif sum == target:
                return ([l+1, r+1])
            else:
                return 0
                
        