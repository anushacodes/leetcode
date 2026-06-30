class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        ans = []
        nums.sort()

        for i, curr in enumerate(nums):
        # add cond to skip elem curr if duplicate
            if i > 0 and (curr == nums[i - 1]):
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                sum = curr + nums[l] + nums[r]
                if sum < 0:
                    l += 1
                elif sum > 0:
                    r -= 1
                elif sum == 0:
                    ans.append([curr, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    # add cond to skip l if duplicate and r if duplicate?
                    # only 1 cond required why?
                    # bc 2nd cond satisfied by above if sum <> 0 loop
                    while (l < r and nums[l] == nums[l - 1]):
                        l += 1

        return ans








