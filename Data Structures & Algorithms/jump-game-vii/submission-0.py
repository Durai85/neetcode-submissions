class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if s[-1] != '0': return False
        queue = deque([0])
        farthest = 0
        n = len(s)
        
        while queue:
            i = queue.popleft()
            left = max(farthest + 1, i + minJump)
            right = min(n-1, i + maxJump)

            for j in range(left, right+1):
                if s[j] == '0':
                    if j == n-1:
                        return True
                    queue.append(j)
                farthest = right
        return False