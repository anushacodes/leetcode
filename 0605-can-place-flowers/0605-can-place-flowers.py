from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        """
        rules:
        1st, atleast 3 0's together
        - 0 0 0 : True
        - 1 0 0 : False BUT 1 0 0 [end]: True
        - 0 0 1 : False BUT [start] 0 0 1 : True
        - 0 1 0 : False
        - 1 1 1 : False
        """

        l = len(flowerbed)

        count = 0

        if l == 1:
            return (flowerbed[0] == 0 and n <= 1) or (flowerbed[0] == 1 and n == 0)

        
        b = [False] * l 

        if l == 2:
            if flowerbed == [0, 0]:
                return n <= 1
            if flowerbed == [1, 0] or flowerbed == [0, 1]:
                return n == 0
            if flowerbed == [1, 1]:
                return n == 0
            return False 

        if l == 3 and n <= 2:
            if flowerbed == [0, 0, 0]:
                return True
        if l == 3 and n ==1:
            if flowerbed == [0, 0, 1]:
                return True
            elif flowerbed == [1, 0, 0]:
                return True
            else:
                return False


        for i in range(1, l-1):

            # start edge case 0 0 1
            if flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 1 and (i == 1):
                print("T: [start] 001")
                b[i-1] = True
                flowerbed[i-1] = 1 

            # start edge case 0 0 0
            elif flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0 and (i == 1):
                print("T: [start] 000")
                b[i-1] = True
                flowerbed[i-1] = 1 

            elif flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                print("T: 000")
                flowerbed[i] = 1
                b[i] = True

            # end edge case
            elif flowerbed[i] == 0 and flowerbed[i-1] == 1 and flowerbed[i+1] == 0 and (i + 2 == len(flowerbed)):
                print("T: 100")
                flowerbed[i+1] = 1
                b[i+1] = True

            else:
                b[i] = False

        final_count = 0
        for val in b:
            # print(f"val: {val}, b: {b}")
            if val:
                final_count += 1

        return final_count >= n
