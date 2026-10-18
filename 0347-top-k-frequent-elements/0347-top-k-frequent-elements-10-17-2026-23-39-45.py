from collections import Counter

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = {}
        res = []

        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        # how to return keys with vals > k???

        # convoluted method bruh
        # for _ in range(k):
        #     num = max(count, key=count.get)
        #     res.append(num)
        #     del count[num]


        sort_counts = sorted(count, key=count.get, reverse=True)
        # print(sort_counts)
        return sort_counts[:k]

        