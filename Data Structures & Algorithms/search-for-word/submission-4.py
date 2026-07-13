class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        dire = [[0,1],[1,0],[-1,0],[0,-1]]
        X,Y = len(board),len(board[0])
        def dfs(i,j,w,vis):
            if w == len(word):
                return True
            if i<0 or j<0 or i == X or j == Y or (i,j) in vis or board[i][j] != word[w]:
                return False
            vis.add((i,j))
            for dx,dy in dire:
                x = i+dx
                y = j+dy
                if dfs(x,y,w+1,vis):
                    return True
            return False
        for row in range(X):
            for col in range(Y):
                if board[row][col] == word[0] and dfs(row,col,0,set()):
                    return True
        return False
                     

                

        