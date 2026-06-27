class Solution:
    def validPalindrome(self, s: str) -> bool:
        s = s.lower()
        l, r = 0, len(s) - 1

        def checkpal(l, r) -> bool:
            while l < r:
                if (s[l] != s[r]):
                    return False
                else:
                    l += 1
                    r -= 1
            return True
            
        while l < r:
            if (s[l] == s[r]):
                l += 1
                r -= 1

            else: 
                return (checkpal(l + 1, r) or checkpal(l, r - 1))
            
        return True    
        