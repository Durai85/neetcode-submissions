from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        m = max(piles)
        left = 1
        right = m - 1
        
        while left <= right:
            mid = (left + right) // 2
            val = 0
            for pi in piles:
                val += ceil(pi / mid)
            
            if val <= h:
                right = mid - 1
            else:
                left = mid + 1

        return left