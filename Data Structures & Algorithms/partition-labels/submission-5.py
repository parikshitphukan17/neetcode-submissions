class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        pos = {}
        N = len(s)
        for i in range(N):
            pos[s[i]] = i
        l,r = 0,0
        res = []
        while l<N:
            r = l
            i = l
            while i<=r and i<N:
                r = max(pos[s[i]],r)
                i+=1
            res.append(r-l+1)
            l = r+1
        return res


        # 0   1   2   3   4   5   6   7   8   9   10  11  12
        # x   y   x   x   y   z   b   z   b   b   i   s   l
        # l1                  l2          
        # r1          r1  r1  r2      r2      r2

        # res = r1-l1+1
