class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        COLS,DiagPos,DiagNeg = set(),set(),set()
      
        res = []
        def dfs(i,cur):
            if i == n:
                res.append(cur.copy())
                return
            for j in range(n):
                if j in COLS or i+j in DiagPos or i-j in DiagNeg :
                    continue
                row = ["."]*n
                row[j] = "Q"
                COLS.add(j)
                DiagPos.add(i+j)
                DiagNeg.add(i-j)
                cur.append("".join(row))
                dfs(i+1,cur)
                COLS.remove(j)
                DiagPos.remove(i+j)
                DiagNeg.remove(i-j)
                cur.pop()
        dfs(0,[])
        return res

                
        