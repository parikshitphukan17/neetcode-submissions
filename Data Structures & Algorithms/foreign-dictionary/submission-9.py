class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = defaultdict(set)
        for i in range(len(words)-1):
            w1,w2 = words[i],words[i+1]
            len1,len2 = len(w1),len(w2)
            minLen=min(len1,len2)
            if w1[:minLen] == w2[:minLen] and len1>len2:
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
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
            vis[src] = True
            res.append(src)
            return True
        for w in words:
            for c in w:
                if not dfs(c):
                    return ""
        return "".join(res[::-1])


        # n->f
        # h->e
        # r->n
        # n->r

        