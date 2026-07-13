class Solution:
    def longestPalindrome(self, s: str) -> str:
        N = len(s)
        def checkPalindrome(i,j):
            res = None
            while i>=0 and j<N and s[i] == s[j] :
                res = [i,j]
                i-=1
                j+=1
            if res:
                return [res[1]-res[0]+1,res]
            else:
                return [0,None]
        resLength = 0
        res = ""
        for i in range(N):
            oddRes = checkPalindrome(i,i)
            evenRes = checkPalindrome(i,i+1)
            curRes = oddRes if oddRes[0] > evenRes[0] else evenRes
            if curRes[0]>resLength:
                resLength = curRes[0]
                res = s[curRes[1][0]:curRes[1][1]+1]
        return res


            


        