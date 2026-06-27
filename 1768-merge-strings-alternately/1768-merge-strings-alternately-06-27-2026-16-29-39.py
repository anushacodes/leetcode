class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = ""

        w1 = len(word1)
        w2 = len(word2)

        shorter = min(w1, w2)

        for i in range(shorter):
            merged += (word1[i])
            merged += (word2[i])

        # join rest of whichever w is longer
        merged += word1[shorter:]
        merged += word2[shorter:]

        return merged

