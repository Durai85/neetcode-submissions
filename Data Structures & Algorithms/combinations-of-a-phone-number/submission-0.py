class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        if digits=='':
            return []
        res, cur = [], []

        def dfs(k):
            if k == len(digits):
                res.append(''.join(cur))
                return

            for i in letters[digits[k]]:
                cur.append(i)
                dfs(k+1)
                cur.pop()

        dfs(0)
        return res