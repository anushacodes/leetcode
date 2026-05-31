class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        # doing this with a new array is easy
        new= []
        for i in range(0, n):
            new.append(nums[i])
            new.append(nums[n+i])
        
        return new

        # trying to do this in the org. array?