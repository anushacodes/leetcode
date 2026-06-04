class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # quicksort does not pass??! (nlog n on avg)
        # merge sort is best (also diff) (nlog n on worst)
        # BST
        # Heapsort idk

        def mergesort(nums):
            # divide array into l, r until atomic numbers remain
            # merge them back up using merge fn
            if len(nums) <= 1:
                return nums

            mid = len(nums) // 2 # int div
            l = nums[0:mid]
            r = nums[mid:len(nums)]
            # recursive part
            l = mergesort(l)
            r = mergesort(r)

            return merge(l, r)



        def merge(l, r):
            res = [] # can this be nums?

            # compare element from both list
            i, j = 0, 0
            while i < len(l) and j < len(r):
            # compare l[i] and r[j]
                if l[i] < r[j]:
                    res.append(l[i])
                    i += 1
                elif r[j] <= l[i]:
                    res.append(r[j])
                    j += 1

            res.extend(l[i:])
            res.extend(r[j:])
        
            return res
        
        return mergesort(nums)


            