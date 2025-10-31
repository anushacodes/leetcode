class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        """
        a = empty string
        choose shorter str1 or str2
        check each iteration of adding a letter from str to a and then 
        check if a*n by round(n) = len(str)/len(a) recreates the str
        if it does then check with other string too
        retunr a

        """

        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        a = ""
        s1 = str1 + str2
        s2 = str2 + str1

        if s1 == s2:
            length = gcd(len(str1), len(str2))
            # return substring of that length
            return str1[:length]

        else:
            return a

        # for letter in 