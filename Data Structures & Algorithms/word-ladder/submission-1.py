class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList.append(beginWord)
        endWordPresent = False
        adj = defaultdict(set)
        for w in wordList:
            if w == endWord:
                endWordPresent = True
            for i in range(len(w)):
                nei = w[:i]+"*"+w[i+1:]
                adj[w].add(nei)
                adj[nei].add(w)
        if not endWordPresent:
            return 0
        q = [beginWord]
        vis = set()
        res =1
        while q:
            child =[]
            while q:
                cur = q.pop()
                if cur in vis:
                    continue
                vis.add(cur)
                if cur == endWord:
                    return res
                for nei in adj[cur]:
                    for w in adj[nei]:
                        child.append(w)
            q = child
            res +=1
        return 0





        # cat -[bat]
        # bat- [bag]
        # bag-[sag,dag]

        # cat


        