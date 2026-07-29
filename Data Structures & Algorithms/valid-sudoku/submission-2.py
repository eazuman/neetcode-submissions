class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        print("Test board",board)
        for item in board:
            print("item",item)
            seen_row = set()
            for n in item:
                if n == ".":
                    continue
                if n in seen_row:
                    return False
                seen_row.add(n)
        for col in range(9):
            print("col is ",col)
            item_seen = set()
            for row in range(9):
                if board[row][col] == "." :
                    continue 
                if board[row][col] in item_seen:
                    return False
                item_seen.add(board[row][col])
            print("final item_seen", item_seen)
                    
        for box_row in range(0, 9, 3):         
            for box_col in range(0, 9, 3): 
                item_seen = set()
                for col in range(3):
                    for row in range(3):
                        value = board[box_row+row][box_col+col]
                        if value == "." :
                            continue 
                        if value in item_seen:
                            return False
                        item_seen.add(value)
                print("final item_seen", item_seen)
        return True
    
        

