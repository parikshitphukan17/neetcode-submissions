class Trie:
    def __init__(self):
        self.child = {}
        self.end = False
    
    def addWord(self,word):
        cur = self
        for c in word:
            if c not in cur.child:
                cur.child[c] = Trie()
            cur = cur.child[c]
        cur.end = True
    




class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for w in words:
            trie.addWord(w)
        
        M,N = len(board),len(board[0])
        resSet= set()
        vis = set()
        dir = [[0,1],[1,0],[-1,0],[0,-1]]
        def dfs(i,j,word,node):
            if i<0 or j<0 or i==M or j==N or (i,j) in vis or  board[i][j] not in node.child:
                return
            vis.add((i,j))
            word += board[i][j]
            node = node.child[board[i][j]]
            if node.end:
                resSet.add(word)
            for dx,dy in dir:
                dfs(i+dx,j+dy,word,node)
            vis.remove((i,j))
            
        for i in range(M):
            for j in range(N):
                dfs(i,j,"",trie)
        return list(resSet)



        