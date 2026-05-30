class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        else:
            # create a dict of all letters here
            # then add frequencies
            # then comapre dicts?
            # return sorted(s) == sorted(t)

            sc = {}
            tc = {}

            for l in s:
                sc[l] = sc.get(l, 0) + 1
                # print("s: ", sc)

            for l in t:
                tc[l] = tc.get(l, 0) + 1
                # print("t: ", tc)

            return sc == tc


            # optim: only 1 dict, do c - 1

            

        