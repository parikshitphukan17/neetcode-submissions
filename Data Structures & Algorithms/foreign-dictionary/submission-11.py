class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = defaultdict(list)
        for i in range(len(words)-1):
            w1,w2 = words[i],words[i+1]
            l1,l2 = len(w1),len(w2)
            minLen = min(l1,l2)
            if w1[:minLen] == w2[:minLen]:
                if l1>l2:
                    return ""

            for i in range(minLen):
                if w1[i] != w2[i]:
                    adj[w1[i]].append(w2[i])
                    break
        vis = {}
        res = []
        def dfs(src):
            if src in vis:
                return vis[src]
            vis[src] = False
            for nei in adj[src]:
                if not dfs(nei):
                    return False
            res.append(src)
            vis[src] = True
            return vis[src]
        for w in words:
            for c in w:
                if not dfs(c):
                    return ""
        return "".join(res[::-1])
            

        