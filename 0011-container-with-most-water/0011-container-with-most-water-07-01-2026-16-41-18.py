class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        cap = 0

        while l < r:
            shorter = min(height[l], height[r])
            width = r - l
            cap = max(cap, shorter * width)
            # print(cap)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return cap

        