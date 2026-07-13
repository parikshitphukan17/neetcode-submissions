class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList.append(beginWord)
        adj = collections.defaultdict(list)
        for w in wordList:
            adj[w] = []
            for i in range(len(w)):
                subText = w[:i] + "*"+w[i+1:]
                adj[w].append(subText)
                adj[subText].append(w)
        vis = set()
        q = [beginWord]
        op = 1
        while q:
            print("op :",op)
            child = []
            print(q)
            for w in q:
                if w == endWord:
                    return op
                vis.add(w)
                for sub in adj[w]:
                    print(sub,adj[sub])
                    for nei in adj[sub]:
                        if nei not in vis:
                            child.append(nei)
            q = child
            op +=1
        return 0

        
        
            

        