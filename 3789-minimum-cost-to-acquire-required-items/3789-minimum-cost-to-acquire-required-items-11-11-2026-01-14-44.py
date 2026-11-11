class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        # either we need both cost1 and cost2 or max(need1, need2) x costBoth
        totalboth = max(need1, need2) * costBoth
        print("both: ", max(need1, need2), costBoth, totalboth)

        totalsep = (cost1 * need1) + (cost2 * need2)
        print("sep: ", (cost1 * need1), (cost2 * need2), totalsep)

        if min(need1, need2) == need1:
            total = need1 * costBoth
            total += (need2 - need1) * cost2
        else:
            total = need2 * costBoth
            total += (need1 - need2) * cost1


        return (min(totalboth, totalsep, total))