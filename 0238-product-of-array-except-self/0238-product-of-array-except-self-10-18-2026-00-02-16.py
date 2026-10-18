class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        mult = 1
        pre, suf = [0] * len(nums), [0] * len(nums)
        ans = [0] * len(nums)

        for i, num in enumerate(nums):
            mult *= num
            pre[i] = mult

        mult = 1
        for i in range(len(nums)-1, -1, -1):
            mult *= nums[i]
            suf[i] = mult

        ans[0] = suf[1]
        ans[len(nums)-1] = pre[-2]
        for i in range(1, len(ans)-1):
            ans[i] = pre[i-1] * suf[i+1]

        return ans



        