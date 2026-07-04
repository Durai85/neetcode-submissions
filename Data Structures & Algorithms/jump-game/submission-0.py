class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0
        n = len(nums)
        for i in range(n):
            if farthest < i:
                return False

            if farthest >= n-1:
                return True

            farthest = max(farthest, nums[i] + i)

        return True