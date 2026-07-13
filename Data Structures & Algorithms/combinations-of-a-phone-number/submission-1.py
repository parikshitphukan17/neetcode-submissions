class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ph = {'2':"abc",'3':"def",'4':"ghi",'5':"jkl",'6':"mno",
        '7':"pqrs",'8':"tuv", '9':"wxyz"}

        res = []
        if not digits:
            return res
        def dfs(i,cur):
            if i == len(digits):
                res.append("".join(cur))
                return
            for char in ph[digits[i]]:
                cur.append(char)
                dfs(i+1,cur)
                cur.pop()
        dfs(0,[])
        return res
        