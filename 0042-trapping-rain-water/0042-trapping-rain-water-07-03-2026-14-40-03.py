class Solution:
    def trap(self, h: List[int]) -> int:
        # water = (min(leftmax, rightmax)) - h[i])
        # not globalmax, localmax, so anything higher than h[i]
        lmax, rmax = [], []
        maxh, water = 0, 0
        for i in range(len(h)):
            maxh = h[i] if maxh < h[i] else maxh
            lmax.append(maxh)
        print (lmax)
        maxh = 0
        for i in range(len(h) - 1, -1, -1):
            maxh = h[i] if maxh < h[i] else maxh
            rmax.append(maxh)
        rmax.reverse()
        print (rmax)

        for i in range(len(h)):
            water += (min(lmax[i], rmax[i]) - h[i])

        return water




        