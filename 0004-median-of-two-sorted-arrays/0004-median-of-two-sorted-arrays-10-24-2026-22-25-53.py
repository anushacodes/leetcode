class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # sort both arrays after merging them - O(m+n)
        # find median of it ?

        nums = nums1 + nums2
        nums.sort()
        mid = len(nums) // 2

        if len(nums) % 2 == 1:
            return nums[mid]
        else:
            return (nums[mid-1] + nums[mid]) / 2
