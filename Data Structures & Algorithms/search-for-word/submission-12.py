class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        dire = [[0,1],[1,0],[0,-1],[-1,0]]
        N,M = len(board),len(board[0])
        vis = set()
        def dfs(i,j,k):
            if k == len(word):
                return True
            if i ==N or j ==M or i<0 or j<0 or board[i][j] != word[k] or (i,j) in vis:
                return False
            vis.add((i,j))
            for dx,dy in dire:
                if dfs(i+dx,j+dy,k+1):
                    return True
            vis.remove((i,j))
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i,j,0):
                    return True
        return False
            





        