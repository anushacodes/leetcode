class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for p in s:
            if p == "(" or p == "[" or p == "{":
                st.append(p)
            elif not st:
                return False
  
            elif ((st[-1] == "(" and p == ")") or
                  (st[-1] == "[" and p == "]") or
                  (st[-1] == "{" and p == "}")):
                st.pop()

            else:
                return False

        return len(st) == 0
        