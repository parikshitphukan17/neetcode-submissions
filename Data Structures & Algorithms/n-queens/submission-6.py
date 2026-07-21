class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        col,posDiag,negDiag = set(),set(),set()
        def dfs(i,cur):
            if i == n:
                res.append(cur.copy())
                return
            row = ["."]*n
            for j in range(n):
                if j in col or i+j in posDiag or i-j in negDiag:
                    continue
                row[j] = "Q"
                cur.append("".join(row))
                col.add(j)
                posDiag.add(i+j)
                negDiag.add(i-j)
                dfs(i+1,cur)
                cur.pop()
                col.remove(j)
                posDiag.remove(i+j)
                negDiag.remove(i-j)
                row[j] = "."
        dfs(0,[])
        return res



                

            
        