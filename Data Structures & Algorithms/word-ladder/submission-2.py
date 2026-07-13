class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if beginWord == endWord:
            return 0
        change = 1
        wordList.append(beginWord)
        endExists =False
        adj = defaultdict(list)
        for word in wordList:
            if word == endWord:
                endExists = True
            for i in range(len(word)):
                n = word[:i]+"*"+word[i+1:]
                adj[word].append(n)
                adj[n].append(word)

        if not endExists:
            return 0
        q = [beginWord]
        vis = set()
        while q:
            child = []
            while q:
                word = q.pop()
                if word in vis:
                    continue
                if word == endWord:
                    return change
                vis.add(word)
                for n in adj[word]:
                    for nn in adj[n]:
                        child.append(nn)
            q = child
            change +=1
        return 0



        