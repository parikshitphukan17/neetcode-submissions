class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c: set() for w in words for c in w}
        for i in range(len(words)-1):
            w1,w2 = words[i],words[i+1]
            len1,len2 = len(w1),len(w2)
            minLen = min(len1,len2)
            if len1>len2 and w1[:minLen] == w2[:minLen]:
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
        

        vis = {}
        res = []
        def dfs(c):
            if c in vis:
                return vis[c]
            vis[c] = False
            for nei in adj[c]:
                if not dfs(nei):
                    return False
            vis[c] = True
            res.append(c)
            return True
        for c in adj:
            if not dfs(c):
                return ""
        return "".join(res[::-1])



        
                


                # {h- [e]
                # r-[n]
                # n - [f]
                # f
                # e-[r]
                
                # }
            
        


        
        