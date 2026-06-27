class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # for i in range(len(s)):
        p1 = 0
        p2 = len(s) - 1
        temp = ""

        while p1 < p2:

            temp = s[p1]
            s[p1] = s[p2]
            s[p2] = temp
            print(s[p1], s[p2])

            p1 += 1
            p2 -= 1

        return s


        