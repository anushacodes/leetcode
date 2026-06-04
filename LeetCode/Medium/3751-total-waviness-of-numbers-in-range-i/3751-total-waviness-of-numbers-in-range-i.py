class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        # 3 pointers, i-1, i, i+1
        # first check if 3 nums exist
        # then iterate through 1, len(num)-1
        # check if i-1 and i+1 are > i or < i


        wav = 0
            
        for num in range(num1, num2 + 1):

            num = str(num)     
            for i in range (1, len(num) - 1):
                l = num[i-1]
                r = num[i+1]
                m = num[i]

                #peak
                if (l > m) and (r > m):
                    wav += 1

                # valley
                elif (l < m) and (r < m):
                    wav += 1

                else:
                    wav += 0

        return wav
                
        