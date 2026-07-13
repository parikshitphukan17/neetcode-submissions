class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        wordList.append(beginWord)
        exists = False
        adj = defaultdict(set)
        for word in wordList:
            if word == endWord:
                exists = True
            for i in range(len(word)):
                nei = word[:i]+"*"+word[i+1:]
                adj[word].add(nei)
                adj[nei].add(word)
        if not exists:
            return 0
        res = 0
        q = deque([])
        q.append(beginWord)
        vis = set()
        while q:
            next = deque([])
            res +=1
            while q:
                cur = q.popleft()
                if cur == endWord:
                    return res
                if cur in vis:
                    continue
                vis.add(cur)
                for nei in adj[cur]:
                    for word in adj[nei]:
                        next.append(word)
            q = next
        return 0
                

#  cat - {bat}
#         bat - {bag,cat}
#         bag - {bat,sag} 
#         sag - {}



#         cat -> {*at,c*t,ca*}
#         bat -> {*at,b*t,ba*}
#         bag -> {*ag,b*g,ba*}
#         sag -> {*ag,s*g,sa*}


#         *at -> {cat,bat}
#         ba* -> {bat,bag}
#         *ag -> {sag,bag}

        # cat -> *at -> bat -> ba*-> bag -> *ag -> sag



       

        


        
        