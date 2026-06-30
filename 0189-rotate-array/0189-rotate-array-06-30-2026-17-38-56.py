class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # temp = nums[k+1:len(nums)]
        # print(temp)
        # l,r = 0, k+1
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]

        # for i in range (k+1):
        #     temp = nums[i]
        #     nums[i] = nums[r]
        #     nums[r] = temp
        #     r += 1

        return nums




        