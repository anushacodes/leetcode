class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest = min(strs, key=len)
        print(shortest)
        res = ""

        for i in range (len(shortest)):
            # compare with rest
            for s in strs:
                if s[i] != shortest[i]:
                    return res

            res += shortest[i]

        return res








        