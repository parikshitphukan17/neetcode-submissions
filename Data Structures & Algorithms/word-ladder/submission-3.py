class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        adj = defaultdict(list)
        wordSet = set(wordList)
        wordSet.add(beginWord)
        if endWord not in wordSet:
            return 0
        for word in wordSet:
            for i in range(len(word)):
                nei = word[:i] + "*" +word[i+1:]
                adj[nei].append(word)
                adj[word].append(nei)

        vis = set()
        res = 1
        q = [beginWord]
        while q:
            print(q)
            nextQ = []
            while q:
                cur = q.pop()
                if cur in vis:
                    continue
                print(cur)
                vis.add(cur)
                if cur == endWord:
                    return res
                for nei in adj[cur]:
                    print("nei",nei)
                    for word in adj[nei]:
                        nextQ.append(word)
            res +=1
            q = nextQ
        return 0
                


        