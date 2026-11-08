class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = defaultdict(list)
        for i in range(len(words)-1):
            w1,w2 = words[i],words[i+1]
            len1,len2 = len(w1),len(w2)
            minLen = min(len1,len2)
            if w1[:minLen] == w2[:minLen] and len1>len2:
                return ""

        
            for j in range(minLen):
                if w1[j]!=w2[j]:
                    adj[w1[j]].append(w2[j])
                    break
        vis = {}
        res = []
        def dfs(c):
            if c in vis:
                return vis[c]
            vis[c] = False
            for nC in adj[c]:
                if not dfs(nC):
                    return False
            vis[c] = True
            res.append(c)
            return True
        for w in words:
            for c in w:
                if not dfs(c):
                    return ""
        return "".join(res[::-1])
        
            

        

    # e    r    n    f
            

    #     n-f
    #     h-e
    #     r-n
    #     e-r
        