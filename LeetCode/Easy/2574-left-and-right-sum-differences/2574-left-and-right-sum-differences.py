class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l, r = [0] * n, [0] * n

        for i in range(1, n):
            # print("i: ", i) 
            l[i] = nums[i - 1] + l[i-1]

        # print(l)

        for i in range(n - 2, -1, -1):
            # print("j: ", i)
            r[i] = nums[i + 1] + r[i+1]
        
        # print(r)

        return [abs(l[i] - r[i]) for i in range (n)]
        