class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # hashmap of nums with frequencies
        # sort that
        # return top k

        freq = {}

        for num in nums:
            # if num not in freq:
            #     freq[num] = 1
            # else:
            #     freq[num] += 1

            freq[num] = freq.get(num, 0) + 1

        # return dict[:k] sorted by items not key
        # list comprehension
        sorted_items = sorted(
            freq.items(),
            key=lambda x: x[1],
            reverse=True
        )

        result = []

        for key, value in sorted_items[:k]:
            result.append(key)

        return result


