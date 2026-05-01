class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        
        s = sum(matchsticks)
        if s % 4 != 0:
            return False

        n = len(matchsticks)
        matchsticks.sort(reverse = True)
        target = s // 4
        bucket = [0] * 4

        def dfs(k):
            if k == n:
                return all(b==target for b in bucket)

            for i in range(4):
                if bucket[i] + matchsticks[k] <= target:
                    if i > 0 and bucket[i] == bucket[i-1]:
                        continue
                    bucket[i] += matchsticks[k]
                    if dfs(k+1):
                        return True
                    bucket[i] -= matchsticks[k]
            
            return False

        return dfs(0)