class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        # [[every subarr mono inc.]]
        # iterate thru arr, take i, then check if next elems are greater, then add to arr2
        # add arr2 to inc arr when next elem is not greater
        # can we check inc and dec in the same loop?
        # vars needed - 
        # 1. inc_res, dec_res, (can be vars tracking max len found instead of arr of arrs)
        # will need temp vars while iterating thru rest of nums after ini. num for idx
        # o(nlog n) ?

        inc = 1
        dec = 1
        maxi = 1

        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                inc += 1
                dec = 1
            elif nums[i] > nums[i + 1]:
                dec += 1
                inc = 1
            else:
                dec = 1
                inc = 1
            
            maxi = max(inc, dec, maxi)


        return maxi

            

            

            
            
            

