class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        vis = set()
        M,N = len(board), len(board[0])
        K = len(word)
        dir = [[0,1],[1,0],[-1,0],[0,-1]]
        def dfs(i,j,k):
            if k == K:
                return True
            if i<0 or j<0 or i >= M or j >=N or (i,j) in vis or word[k]!= board[i][j]:
                return False
            vis.add((i,j))
            for dx,dy in dir:
                if dfs(i+dx,j+dy,k+1):
                    return True
            vis.remove((i,j))
            return False
        for i in range(M):
            for j in range(N):
                if dfs(i,j,0):
                    return True
        return False
            


        