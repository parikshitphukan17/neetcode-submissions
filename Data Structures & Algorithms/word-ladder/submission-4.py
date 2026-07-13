class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList.append(beginWord)
        adj = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                nei = word[:i]+"*"+word[i+1:]
                adj[word].append(nei)
                adj[nei].append(word)
        q = deque([beginWord])
        if beginWord == endWord:
            return 0
        res = 1
        vis = set()
        vis.add(beginWord)
        while q:
            child = deque([])
            while q:
                word = q.popleft()
                if word == endWord:
                    return res
                for n in adj[word]:
                    for nei in adj[n]:
                        if nei in vis:
                            continue
                        vis.add(nei)
                        child.append(nei)
            res += 1
            q=child
        return 0



        # cat
        # *at- [cat,bat]
        # c*t- [cat]
        # ca*- [cat]
        # b*t- [bat]
        # ba*- [bat,bag]
        # *ag- [bag,sag,dag]
        # b*g- [bag]
        # s*g- [sag]
        # sa*- [sag]
        # da*- [dag]
        # d*g- [dag]

        # 1                       2                       3               4
        # cat-> [*at, c*t,ca*]-> [bat]-> [b*t,*at,ba*]-> [bag]-> [*ag]-> [sag]




        