class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        dire = [[0,1],[0,-1],[1,0],[-1,0]]
        N,M = len(board),len(board[0])
        l=len(word)
        def dfs(i,j,index,vis):
            if index == l:
                return True
            if (i,j) in vis or i<0 or i==N or j<0 or j==M or board[i][j] != word[index]:
                return False
            vis.add((i,j))
            for dx,dy in dire:
                if dfs(i+dx,j+dy,index+1,vis):
                    return True
            vis.remove((i,j))
            return False
        for x in range(len(board)):
            for y in range(len(board[0])):
                if dfs(x,y,0,set()):
                    return True
        return False
        
            
            
            


        