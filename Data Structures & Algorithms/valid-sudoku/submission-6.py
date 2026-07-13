class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowSet = [set() for _ in range(len(board))]
        colSet = [set() for _ in range(len(board[0]))]



        for row in range(0,len(board),3):
            for col in range(0,len(board[0]),3):
                vis = set()
                for r in range(row,row+3,1):
                    for c in range(col,col+3,1):
                        
                        cur =  board[r][c]
                        if cur == ".":
                            continue
                        if cur in rowSet[r] or cur in colSet[c] or cur in vis:
                            return False
                        rowSet[r].add(cur)
                        colSet[c].add(cur)
                        vis.add(cur)
        return True



        