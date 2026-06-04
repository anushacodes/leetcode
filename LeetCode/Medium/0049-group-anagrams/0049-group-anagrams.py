from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for word in strs:
            # key = sorted word
            # value = word itself
            key = tuple(sorted(word))
            if key not in d:
                d[key] =[]
            d[key].append(word)
        
        return (list(d.values()))
                


        