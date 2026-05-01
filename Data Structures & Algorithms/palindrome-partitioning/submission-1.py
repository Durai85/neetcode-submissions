class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result, cur = [], []

        def dfs(start):
            if start == len(s):
                result.append(cur[:])
                return
            
            for end in range(start,len(s)):
                if isPalindrome(s[start:end+1]):
                    cur.append(s[start:end+1])
                    dfs(end+1)
                    cur.pop()

        def isPalindrome(s):
            return s == s[::-1]

        dfs(0)
        return result