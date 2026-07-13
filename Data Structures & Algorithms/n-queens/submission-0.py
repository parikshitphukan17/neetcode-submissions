class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.res = []
        self.nq(0,0,n,[],set(),set(),set())
        return self.res.copy()

    def nq(self,i,j,n,cur,vis,l,b):
        #print(cur)
        def dfs(i,j,vis,l,b):
            if i in l or j in b:
                return False
            xCpy ,yCpy = i,j
            while xCpy-1>=0 and yCpy-1>=0:
                
                xCpy-=1
                yCpy-=1
                if (xCpy,yCpy) in vis:
                    return False
            
            xCpy ,yCpy = i,j
            while xCpy-1>=0 and yCpy+1<n:
                xCpy-=1
                yCpy+=1
                if (xCpy,yCpy) in vis:
                    return False
            return True
        if i==n:
            self.res.append(cur.copy())
            return

        row =["."]*n
        for y in range(n):
            if not dfs(i,y,vis,l,b):
                continue
            row[y]="Q"
            cur.append("".join(row))
            vis.add((i,y))
            l.add(i)
            b.add(y)
            self.nq(i+1,0,n,cur,vis,l,b)
            row[y]="."
            vis.remove((i,y))
            l.remove(i)
            b.remove(y)
            cur.pop()
    
        

        



        



        