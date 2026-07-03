class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        possible = 0
        l = 0

        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
                print(s[l], s[r], possible)

            seen.add(s[r])
            possible = max(possible, r - l + 1)
            print("out: ", s[l], s[r], possible)

        return possible


        