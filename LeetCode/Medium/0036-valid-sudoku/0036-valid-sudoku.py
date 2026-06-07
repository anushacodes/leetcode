class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        print(board)


        # check rows
        for row in range(9):
            seen = set() 
            for col in range(9):
                num = board[row][col] 
                
                if num == ".":
                    continue
                elif num in seen:
                    return False
                    break
                else:
                    seen.add(num)

        # check cols
        for col in range(9):
            seen = set() 
            for row in range(9):
                num = board[row][col] 
                
                if num == ".":
                    continue
                elif num in seen:
                    return False
                else:
                    seen.add(num)

        # check boxes
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                seen = set()

                for r in range(box_row, box_row + 3):
                    for c in range(box_col, box_col + 3):
                        num = board[r][c]
                    
                        if num == ".":
                            continue
                        elif num in seen:
                            return False
                        else:
                            seen.add(num)

        return True

                

            

        