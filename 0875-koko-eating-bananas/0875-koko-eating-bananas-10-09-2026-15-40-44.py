class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        # search space - 1 to max(piles) since h is atleast len(piles)
        l, r = 1, max(piles)
        res = r

        # bin search thru search space
        while l <= r:
            mid = (l+r) // 2
            # Calculate the total hours needed at this speed without changing the piles
            hrs, total = 0, 0
            for pile in piles:
                hrs = (pile +mid - 1) // mid
                total += hrs
            # print(mid, total)
            
            if total > h:
                l = mid + 1
            else:
                res = mid
                r = mid - 1

        return res
            


            




        