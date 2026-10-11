class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        hm = {}

        for i, s in enumerate(strs):
            ss = "".join(sorted(s))
            if ss in hm:
                hm[ss].append(s)

            else:
                hm[ss] = [s]

        return (list(hm.values()))