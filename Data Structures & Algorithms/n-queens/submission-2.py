class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col,diagP,diagN = set(),set(),set()
        res = []
        def dfs(i,cur):
            if i == n:
                res.append(cur.copy())
                return
            row = ["."]*n
            for j in range(n):
                if (i+j) in diagP or (i-j) in diagN or j in col:
                    continue
                row[j] = "Q"
                diagP.add((i+j))
                diagN.add((i-j))
                col.add(j)
                cur.append("".join(row))
                dfs(i+1,cur)
                diagP.remove((i+j))
                diagN.remove((i-j))
                col.remove(j)
                row[j] = "."
                cur.pop()
        dfs(0,[])
        return res
            





        