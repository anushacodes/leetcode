class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # n = 1

        # for num in nums:
        #     n *= num

        res = [1] * len(nums)

        # for num in nums:
        #     res.append(n // num)

        # return res

        right = [1] * len(nums)
        left = [1] * len(nums)

        #left
        for i in range (1, len(nums)):
            left[i] = nums[i-1] * left[i-1]

        # print(left)


        # right
        for i in range (len(nums)-2, -1, -1):
            right[i] = nums[i+1] * right[i+1]

        # print(right)

        
        for i in range(len(nums)):
            res[i] = right[i] * left[i]

        return res



            
        