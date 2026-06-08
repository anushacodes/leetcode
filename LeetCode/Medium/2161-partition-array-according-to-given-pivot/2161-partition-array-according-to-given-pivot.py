class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        # 2 pointers nope because idk how many spaces needed before and after the pivot

        # 2 arrays, less and more

        less, more = [], []
        c = 0

        for num in nums:
            if num < pivot:
                less.append(num)
            elif num > pivot:
                more.append(num)
            else:
                c += 1

        for i in range(c):
            less.append(pivot)

        return less+ more
        