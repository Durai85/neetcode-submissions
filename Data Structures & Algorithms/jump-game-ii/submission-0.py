class Solution:
    def jump(self, nums: List[int]) -> int:
        farthest = 0
        currentEnd = 0
        jumps = 0
        n = len(nums)
        for i in range(n-1):
            farthest = max(farthest, nums[i]+i)
            if i == currentEnd:
                currentEnd = farthest
                jumps += 1

        return jumps