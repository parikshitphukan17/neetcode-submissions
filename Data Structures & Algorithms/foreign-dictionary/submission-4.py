class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c:set() for w in words for c in w}
        for i in range(len(words)-1):
            word1,word2 = words[i],words[i+1]
            len1,len2 = len(word1),len(word2)
            minLen = min(len1,len2)
            if len1>len2 and word1[:minLen] == word2[:minLen]:
                return ""
            j = 0
            while j<minLen:
                if word1[j] != word2[j]:
                    adj[word1[j]].add(word2[j])
                    break
                j+=1
        vis = {}
        res = []
        def dfs(char):
            if char in vis:
                return vis[char]
            vis[char] = True
            for nei in adj[char]:
                if dfs(nei):
                    return True
            vis[char] = False
            res.append(char)
            return False
        
        for w in adj:
            if dfs(w):
                return ""
        res.reverse()
        return "".join(res)
        
            
            


        