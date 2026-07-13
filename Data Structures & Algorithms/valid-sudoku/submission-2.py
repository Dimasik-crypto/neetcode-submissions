class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for row in board:
            nums = [int(x) for x in row if x != '.']
            if len(nums) != len(set(nums)):
                return False

        
        for j in range(9):
            col = [board[i][j] for i in range(9)]  
            nums = [int(x) for x in col if x != '.']
            if len(nums) != len(set(nums)):
                return False

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                box = []
                for x in range(3):
                    for y in range(3):
                        box.append(board[i+x][j+y])
               
                nums = [int(x) for x in box if x != '.'] 
                if len(nums) != len(set(nums)):
                    return False

        return True