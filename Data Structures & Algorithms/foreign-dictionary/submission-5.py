class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c: set() for w in words for c in w}

        for i in range(len(words)-1):
            w1 = words[i]
            w2 = words[i+1]
            minLen= min(len(w1),len(w2))
            if len(w1)>len(w2) and w1[:minLen] == w2[:minLen]:
                return ""

            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break

        vis = {}
        res = []
        def dfs(src):
            print(src)
            if src in vis:
                return vis[src]
            vis[src] = False
            for nei in adj[src]:
                if not dfs(nei):
                    return False
            vis[src] = True
            res.append(src)
            return True
        print(adj)
        for src in adj:
            if not dfs(src):
                return ""
            print(res)
        res.reverse()
        return "".join(res)
                
            
        


        
        