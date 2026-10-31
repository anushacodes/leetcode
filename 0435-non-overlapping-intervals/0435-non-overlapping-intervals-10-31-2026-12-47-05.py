class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda intervals: intervals[1])
        # print(intervals)
        skip = 0
        last = float("-inf")

        for start, end in intervals:
            if start < last:
                skip += 1
            else:
                last = end

        return skip


