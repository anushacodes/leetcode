class Solution:
    def calPoints(self, ops: List[str]) -> int:
        # D -> double prev score
        # C -> remove last score
        # + -> sum prev 2 scores

        st = []

        for op in ops:
            if op.isnumeric() == True or op[0]=="-" and op[1:].isnumeric():
                print("op isnum:", op)
                st.append(int(op))
                print(st)

            elif op == 'D':
                print("op D:", op)
                st.append(2*int(st[-1]))
                print(st)

            elif op == 'C':
                print("op C:", op)
                st.pop()
                print(st)

            elif op == '+':
                print("op +:", op)
                st.append(int(st[-1]) + int(st[-2]))
                print(st)


        # sum = 0
        # for i in st:
        #     sum += int(i)
        return sum(st)


            
