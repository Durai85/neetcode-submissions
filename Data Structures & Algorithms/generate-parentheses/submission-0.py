class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def dfs(open, close, current):
            if len(current) == 2*n:
                result.append(current[:])
                return

            if open < n:
                dfs(open+1,close,current+'(')
            if close < open:
                dfs(open,close+1,current+')')

        dfs(0,0,'')
        return result