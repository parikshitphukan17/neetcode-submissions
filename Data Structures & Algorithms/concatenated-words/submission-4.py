class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        wordset = set(words)
        dp = {}
        def dfs(word):
            if word in dp:
                return dp[word]
            for i in range(len(word)):
                prefix,suffix = word[:i],word[i:]
                if ((prefix in wordset and suffix in  wordset)
                or (prefix in wordset and dfs(suffix))):
                    dp[word] = True
                    return True
            dp[word] = False
            return False

            
        
        res = []
        for w in words:
            if dfs(w):
                res.append(w)
        return res

                    
                


        # catsdogcats 


        # cat sdog -> ....
        # cats dogcats 
        # cat -X
        # dog cats ->

        # def check(word,first):
        #     iterate thorugh list of words
        #     check if eligible and reach end 
        #      yes -> return not first:
        #      if not reach end do recursion and set first as false

        
    
        # dogcatsdog
        # ratcatdogcat





        