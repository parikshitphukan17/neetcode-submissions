class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowVal = [set() for _ in range(len(board))]
        colVal = [set() for _ in range(len(board))]

        for i in range(0,len(board),3):
            for j in range(0,len(board),3):
                visBoard = set()
                for boardI in range(i,i+3,1):
                    for boardJ in range(j,j+3,1):
                        val = board[boardI][boardJ]
                        if val == ".":
                            continue
                        if val in rowVal[boardI] or val in colVal[boardJ] or val in visBoard:
                            return False
                        rowVal[boardI].add(val)
                        colVal[boardJ].add(val)
                        visBoard.add(val)
        return True

        