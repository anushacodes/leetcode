from collections import Counter

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        sneaks = []
        c = Counter()

        for n in nums:
            c[n] += 1

        for k, v in c.items():
            if v != 1:
                sneaks.append(k)


        return sneaks   

                

            

            
