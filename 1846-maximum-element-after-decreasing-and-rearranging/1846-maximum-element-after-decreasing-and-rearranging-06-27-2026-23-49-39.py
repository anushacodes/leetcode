class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        # # abs diff btw 2 adj nums <= 1
        # def decrease(arr):

        # # bring 1 to index 0 if it exists
        # def rearr()

        arr.sort()

        if arr[0] != 1:
            arr[0] = 1

        for i in range (len(arr)-1):
            if (abs(arr[i] - arr[i + 1]) > 1):
                arr[i + 1] = arr[i] + 1
    
        # print
            
        return arr[len(arr) - 1]






