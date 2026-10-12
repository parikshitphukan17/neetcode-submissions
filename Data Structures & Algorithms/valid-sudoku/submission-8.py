class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        col = defaultdict(set)
        for r in range(0,9,3):
            for c in range(0,9,3):
                subBox = set()
                for i in range(r,r+3,1):
                    for j in range(c,c+3,1):
                        val = board[i][j]
                        if val == ".":
                            continue
                        if val in subBox or val in row[i] or val in col[j]:
                            return False
                        subBox.add(val)
                        row[i].add(val)
                        col[j].add(val)
        return True
        