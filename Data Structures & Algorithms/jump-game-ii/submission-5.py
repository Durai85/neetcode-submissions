class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        jumps = 1
        farther = 0
        boundary = nums[0]

        for i in range(n-1):
            farther = max(nums[i] + i, farther)
            if i == boundary:
                jumps += 1
                boundary = farther

        return jumps