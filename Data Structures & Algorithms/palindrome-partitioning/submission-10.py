class Solution:
    def partition(self, s: str) -> List[List[str]]:
        N = len(s)
        res = []
        def dfs(i,cur):
            if i==N:
                res.append(cur.copy())
                return
            sub = ""
            rev = ""
            for j in range(i,N):
                sub += s[j]
                rev = s[j]+rev
                if sub==rev:
                    cur.append(sub)
                    dfs(j+1,cur)
                    cur.pop()
        dfs(0,[])
        return res

        # aab


        # 0,3 []
        # s=a
        # r=a


        # 1,3 [a]
        # s=a
        # r=a

        # 2,3 [a,a]
        # s=b
        # r=b 

        # 3,3 [a,a,b]


        # 2,3 [a]


        