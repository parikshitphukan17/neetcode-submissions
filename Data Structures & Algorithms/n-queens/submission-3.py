class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        posDiag = set()
        negDiag = set()
        col = set()
        res = []

        def dfs(i,cur):
            nonlocal n
            if i == n:
                res.append(cur.copy())
                return
            
            for j in range(n):
                if i+j in posDiag or i-j in negDiag or j in col:
                    continue
                posDiag.add(i+j)
                negDiag.add(i-j)
                col.add(j)
                row = ["."]*n
                row[j] = "Q"
                cur.append("".join(row))
                dfs(i+1,cur)
                cur.pop()
                col.remove(j)
                posDiag.remove(i+j)
                negDiag.remove(i-j)

        dfs(0,[])
        return res
                

        # 0-2 = 1-3 = -2
        # 0,2
        # 1,1, 1,3
        # 2,0. 


        # 0,0 1,1.                             0,3. 1,2, 2,1
        # 2,2
        # 3,3


        # 0,2 0+2 = 1+1 = 2,0
        # 1,1


        