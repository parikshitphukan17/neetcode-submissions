class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        posDiag,negDiag,col= set(),set(),set()
        def dfs(i,cur):
            if i == n:
                res.append(cur.copy())
                return
            row = ["."]*n
            for j in range(n):
                if j in col or i+j in posDiag or i-j in negDiag:
                    continue
                col.add(j)
                posDiag.add(i+j)
                negDiag.add(i-j)
                row[j] = "Q"
                cur.append("".join(row))
                dfs(i+1,cur)
                cur.pop()
                row[j] = "."
                col.remove(j)
                posDiag.remove(i+j)
                negDiag.remove(i-j)
        dfs(0,[])
        return res
                

            

        # 0,0         0,2
        #     1,1
        # 2,0
        

        # sum - posDiag
        # neg - negDiag