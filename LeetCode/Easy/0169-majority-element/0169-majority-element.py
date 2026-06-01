class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        m = len(nums)
        mid = int(m / 2)
        snums = sorted(nums)
        # print(mid)

        return snums[mid]
