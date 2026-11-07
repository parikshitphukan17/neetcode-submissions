class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        adj = defaultdict(list)
        wordSet = set(wordList)
        wordSet.add(beginWord)
        for w in wordSet:
            for i in range(len(w)):
                nei = w[:i]+"*"+w[i+1:]

                adj[nei].append(w)
                adj[w].append(nei)
        res = 0
        if endWord not in adj.keys():
            return res
        q = [beginWord]
        vis = set()
        while q:
            nextQ = []
            while q:
                word = q.pop()
                if word in vis:
                    continue
                if word == endWord:
                    return res+1
                vis.add(word)
                for nei in adj[word]:
                    for nextNei in adj[nei]:
                        nextQ.append(nextNei)
            q = nextQ
            res +=1
        return 0



        