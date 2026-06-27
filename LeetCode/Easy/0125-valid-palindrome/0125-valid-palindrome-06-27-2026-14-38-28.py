class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        l, r = 0, len(s) - 1
        flag = True

        while l < r:
            if not s[l].isalnum():
                l += 1
            if not s[r].isalnum():
                r -= 1
            
            if s[l].isalnum() and s[r].isalnum():
                if (s[l] == s[r]):
                    l += 1
                    r -= 1
                    
                else:
                    flag = False
                    break

        return flag        