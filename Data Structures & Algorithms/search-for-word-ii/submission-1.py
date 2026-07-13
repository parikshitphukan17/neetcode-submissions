class TreeNode:
    def __init__(self):
        self.child = {}
        self.word = False
    def addWord(self,word):
        cur = self
        for w in word:
            if w not in cur.child:
                cur.child[w] = TreeNode()
            cur = cur.child[w]
        cur.word = True

    

    

class Solution:
    def __init__(self):
        self.root = TreeNode()
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        N,M = len(board),len(board[0])
        res = set()
        vis = set()
        def dfs(r,c,word,node):
            if r<0 or r==N or c<0 or c==M or (r,c) in vis or not node.child or board[r][c] not in node.child:
                return
            word += board[r][c]
            vis.add((r,c))
            node = node.child[board[r][c]]
            if node.word:
                res.add(word)
            dfs(r+1,c,word,node)
            dfs(r-1,c,word,node)
            dfs(r,c+1,word,node)
            dfs(r,c-1,word,node)
            vis.remove((r,c))
        for w in words:
            self.root.addWord(w)
        for i in range(N):
            for j in range(M):
                dfs(i,j,"",self.root)
        return list(res)
        