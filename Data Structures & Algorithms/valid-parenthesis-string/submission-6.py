class Solution:
    def checkValidString(self, s: str) -> bool:
        dp = {}
        def dfs(i,cur):
            if cur<0:
                return False
            if i == len(s):
                return cur == 0
            if (i,cur) in dp:
                return dp[(i,cur)]
            if s[i] == "(":
                dp[(i,cur)] = dfs(i+1,cur+1)
            elif s[i] == ")":
                dp[(i,cur)] = dfs(i+1,cur-1)
            else:
                dp[(i,cur)] = dfs(i+1,cur+1) or dfs(i+1,cur-1) or dfs(i+1,cur)
            return dp[(i,cur)]
        return dfs(0,0)
        